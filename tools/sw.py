#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sw.py — Agent-InsightDashboard-Sunwoo.

MOT lan doc  ->  out/doc-hoi-thoai.json  ->  insight / qc, TUNG DONG rieng.

    python tools/sw.py doc     du-lieu/hoi-thoai.md --ky "28/10-03/11"
    python tools/sw.py insight --dong a
    python tools/sw.py qc      --dong d
    python tools/sw.py kiem    out/insight-a.json

HAI TUONG (sw-F):
  · TUONG D (dong)  — chan PHEP CHIA: ⛔ khong ty le nao tron mau so a+d
  · TUONG L (luong) — chan TRUONG   : ⛔ khong file nao co ca ten NV va loi khach

⛔ Moi lan ghi JSON di qua ghi_json(). Truot CONG T -> sys.exit(2).
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import unicodedata

for _l in (sys.stdout, sys.stderr):
    try:
        _l.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(GOC, "out")
TD = {}

# Ten hien thi co dau cho ma rao / ma co do (tu dien luu dang khong dau)
TEN_RAO = {"SO": "SỢ", "NGO": "NGỜ", "NGAI": "NGẠI", "BEN": "BỀN", "LAU": "LÂU"}
TEN_CO = {("CD-S%d" % i): ("CĐ-S%d" % i) for i in range(1, 11)}

CHAN_BANG = ("Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay "
             "xếp hạng công khai.")
CAU_MAU = ("Mẫu kỳ này chỉ gồm hội thoại tiếng Anh. ⛔ Chưa đọc được: "
           "Taglish · Filipino · Hàn · Farsi. Vì vậy ⛔ không kết luận về nhóm "
           "N1, và số của V3 có thể đang đọc thiếu.")


# ────────────────────────────────────────────────────────────────────
# 1 · KHOP TIENG ANH  (sw-B §6 — ba bay)
# ────────────────────────────────────────────────────────────────────

_RE = {}


def chuan(s):
    """Ha chu, bo dau nguoc/xuoi, bo dau cau don gian. ⛔ KHONG bo ranh gioi tu."""
    s = (s or "").lower().replace("’", "").replace("'", "")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def _re_cum(cum):
    """Regex khop CUM theo RANH GIOI TU, cho phep <=2 tu chen giua (bay ②)."""
    r = _RE.get(cum)
    if r is None:
        tu = chuan(cum).split()
        than = r"\s+(?:[\w\-]+\s+){0,2}".join(re.escape(t) for t in tu)
        r = re.compile(r"(?<![\w\-])" + than + r"(?![\w\-])")
        _RE[cum] = r
    return r


def chua(text, ds):
    """True neu text chua BAT KY cum nao trong ds — khop theo ranh gioi tu.

    ⛔ KHONG dung `cum in text`: "pain" in "painless" la True, ma "painless"
    mang nghia NGUOC va nam trong bang tu cam (sw-B §6 bay ①).
    """
    t = chuan(text)
    for cum in ds or []:
        if _re_cum(cum).search(t):
            return True
    return False


def cum_khop(text, ds):
    t = chuan(text)
    return [c for c in (ds or []) if _re_cum(c).search(t)]


def nap_tu_dien():
    global TD
    p = os.path.join(GOC, "tools", "tu_dien.json")
    with io.open(p, encoding="utf-8") as f:
        TD = json.load(f)
    return TD


# ────────────────────────────────────────────────────────────────────
# 2 · DOC FILE HOI THOAI
# ────────────────────────────────────────────────────────────────────

RE_DAU = re.compile(
    r"^###\s*(HT-\d+)\s*\|\s*([\d\-/]+)\s*(?:([\d:]+))?\s*\|\s*(\w+)"
    r"(?:\s*\|\s*NV:\s*([^|]+?))?(?:\s*\|\s*post:\s*([^|]+?))?\s*$")
RE_THE = re.compile(r"^\s*\[\s*Thẻ\s*:", re.I)


def doc_file(path):
    """Tra ve list dict tho. ⚠ Dong [The: ...] ⛔ KHONG phai mot luot khach."""
    with io.open(path, encoding="utf-8") as f:
        dong = f.read().splitlines()

    ds, ht = [], None
    for d in dong:
        m = RE_DAU.match(d.strip())
        if m:
            ht = {
                "ht": m.group(1),
                "ngay": m.group(2),
                "gio": m.group(3) or "",
                "kenh": (m.group(4) or "").lower(),
                "nv": (m.group(5) or "").strip(),
                "post_ads": (m.group(6) or "").strip(),
                "kh": [], "nv_noi": [], "the": [],
            }
            ds.append(ht)
            continue
        if ht is None:
            continue
        s = d.strip()
        if not s:
            continue
        if RE_THE.match(s):
            ht["the"].append(s)          # ★ ghi chu he thong, ⛔ KHONG dem
        elif s.startswith("KH:"):
            noi = s[3:].strip()
            if noi:
                ht["kh"].append(noi)     # ★ chi dem luot khach THAT
        elif s.startswith("NV:"):
            noi = s[3:].strip()
            if noi:
                ht["nv_noi"].append(noi)
    return ds


# ────────────────────────────────────────────────────────────────────
# 3 · GAN DU KIEN
# ────────────────────────────────────────────────────────────────────

def gan_dong_hoi(loi_kh):
    """★ Tra ve LIST — hoi thoai hoi ca hai dong thi ["a","d"] (sw-D §2)."""
    ra = []
    for d in ("a", "d"):
        if chua(loi_kh, TD["dong"][d]):
            ra.append(d)
    return ra


def gan_dv(loi_kh, dong):
    """Ma dich vu trong dong da cho. ⛔ Ngoai danh sach -> DV-A0 / DV-D0."""
    tien_to = "DV-A" if dong == "a" else "DV-D"
    ra = [k for k, v in TD["dv"].items() if k.startswith(tien_to) and chua(loi_kh, v)]
    return ra or [tien_to + "0"]


def gan_chang(loi_kh, dong):
    """Chang CAO NHAT khach da toi. S1–S6 cho dong a, SD1–SD6 cho dong d."""
    bo = ["S1", "S2", "S3", "S4", "S5", "S6"] if dong == "a" else \
         ["SD1", "SD2", "SD3", "SD4", "SD5", "SD6"]
    thay = [c for c in bo if chua(loi_kh, TD["chang"][c])]
    return thay[-1] if thay else bo[0]


def gan_rao(loi_kh, dong):
    """Rao nang nhat. ⚠ Dong a dung BEN, dong d dung LAU — ⛔ khong tron."""
    uu = ["LAU", "NGAI", "SO", "NGO"] if dong == "d" else ["BEN", "SO", "NGAI", "NGO"]
    for r in uu:
        if chua(loi_kh, TD["rao"][r]):
            return TEN_RAO[r]
    return ""


def gan_vanh_dai(loi_kh):
    """V1–V4, ⛔ khong thay dau hieu nao -> V0 (⛔ KHONG doan). CONG G."""
    for v in ("V1", "V2", "V3", "V4"):
        if chua(loi_kh, TD["vanh_dai"][v]):
            return v
    return "V0"


def gan_nhom(loi_kh):
    for n in ("N1", "N2", "N3"):
        if chua(loi_kh, TD["nhom"][n]):
            return n
    return ""


def gan_lam_o_dau(loi_kh):
    """★ sw-C §6 — du kien DOC LAP, ⛔ KHONG khoa sau ma dich vu nao.

    Nhan bang LOGIC: can mot dau hieu "da lam" + mot chi dau noi lam.
    ⚠ Loi da xay ra that o repo khac: gan ham nay SAU khi ma dich vu da
      roi vao mot nhom nhat dinh -> hoi thoai PHAN ANH bi cham nhu mot
      co hoi ban.
    """
    t = TD["lam_o_dau"]
    da_lam = chua(loi_kh, t["dau_hieu_da_lam"])
    # ⚠ CA HAI nhanh deu phai co dau hieu "DA LAM".
    #   Loi tim ra khi chay thu: "is your clinic HMO-accredited?" khop
    #   "your clinic" nen bi gan `tai-sunwoo` — trong khi do la mot cau
    #   HOI cua khach MOI, ⛔ khong phai mot ca da lam tai co so.
    if chua(loi_kh, t["tai_sunwoo"]) and da_lam:
        return "tai-sunwoo"
    if chua(loi_kh, t["noi_khac"]) and da_lam:
        return "noi-khac"
    return ""


def gan_nhan_ht(loi_kh, lod, co_cap_tinh=False):
    """★ `tai-sunwoo` MOT MINH ⛔ KHONG phai phan anh.

    Loi tim ra khi chay thu: mot khach QUAY LAI (da lam cleaning o day,
    nay hoi veneer) bi gan nhan "phan anh" chi vi lam_o_dau = tai-sunwoo.
    ⚠ Gan sai theo chieu nay lam MAT o `cheo` — tai san rieng cua co so
      hai dong — va bien mot ca ban them thanh mot ca khieu nai.

    ★ Phai co `tai-sunwoo` + DAU HIEU VAN DE moi la phan-anh.
    """
    if lod != "tai-sunwoo":
        return ""
    # ★ Bien chung CAP TINH sau mot ca lam TAI co so la HAU MAI theo dinh
    #   nghia — ⛔ khong bao gio la mot ca quay lai de ban them.
    if co_cap_tinh:
        return "phan-anh"
    if chua(loi_kh, TD["lam_o_dau"]["dau_hieu_van_de"]):
        return "phan-anh"
    return "quay-lai"


def an_toan_bac(loi_kh, dong):
    """★ HAI BAC (sw-C §5). Chi `cap-tinh` moi kich hoat luong ⛔ khong ban.

    bay ①: tu cua CHI DINH LAM LAI ⛔ KHONG phai cap tinh — do la CD-D5,
            chan dung dat nhat dong d. Gan sai = MAT PHAN KHEN DUNG.
    bay ②: mot dau hieu DON LE chua du — phai co DAU HIEU + DANG DIEN TIEN.
    """
    t = TD["an_toan"]
    if chua(loi_kh, t["khong_phai_cap_tinh"]):
        return ""
    ds = t["d_dau_hieu"] if dong == "d" else t["a_dau_hieu"]
    if not chua(loi_kh, ds):
        return ""
    return "cap-tinh" if chua(loi_kh, t["dien_tien"]) else "can-bs"


BIT = ["t1_dich_vu", "t2_tien", "t3_thoi_gian", "t4_khu_vuc_lich", "t5_dat_lich"]


def cham_bitmask(loi_kh, dv):
    """5 tin hieu -> list bool. Bit ① = neu dung MOT dich vu cu the."""
    co_dv = bool([x for x in dv if not x.endswith("0")])
    return [co_dv] + [chua(loi_kh, TD["tin_hieu"][b]) for b in BIT[1:]]


def hot_sao(bits, bo_bit):
    """★ sw-I2 §3 — HOT* tinh lai ⛔ KHONG co bit bi cach chia nhom cay vao."""
    return sum(1 for i, b in enumerate(bits) if b and (i + 1) not in bo_bit)


BO_BIT = {"dv": {1}, "chang": {2, 3}, "rao": {2, 3}, "vanh_dai": {4},
          "nhom": {4}, "cd": {1, 2, 3}}


# ────────────────────────────────────────────────────────────────────
# 4 · CO DO  (sw-Q2 — MIEN TRU XET TRUOC)
# ────────────────────────────────────────────────────────────────────

def mien_tru(ma, cau):
    """★ Luat nang nhat: xet mien tru TRUOC khi neu co.

    "we don't guarantee" chua "guarantee"; "let me confirm" la cach xu ly
    DUNG khi slot con treo. Neu co cho nhung cau do la loi NANG NHAT he
    nay co the mac — nang hon bo sot mot co.
    """
    mt = TD["mien_tru"]
    return chua(cau, mt.get("chung", [])) or chua(cau, mt.get(ma, []))


def soat_co_do(loi_nv):
    """Tra ve list (ma_hien_thi, cau_nguyen_van)."""
    ra = []
    for cau in loi_nv:
        for ma, ds in TD["co_do"].items():
            if chua(cau, ds) and not mien_tru(ma, cau):
                ra.append((TEN_CO[ma], cau))
    return ra


# ────────────────────────────────────────────────────────────────────
# 5 · CHAM TC-1…TC-10  (sw-Q1)
# ────────────────────────────────────────────────────────────────────

def _phut(gio):
    try:
        h, m = gio.split(":")[:2]
        return int(h) * 60 + int(m)
    except (ValueError, AttributeError):
        return None


def trong_gio(gio):
    p = _phut(gio)
    if p is None:
        return None
    ng = TD["nguong"]
    return ng["gio_mo"] * 60 <= p < ng["gio_dong"] * 60


def cham_tc(ht, dong, slot_treo=True):
    """10 o. "—" = ⛔ KHONG cham duoc, ⛔ KHONG phai o truot.

    ★ O "—" ⛔ KHONG vao mau so. Dua no vao mau so la tru diem nguoi vi
      mot viec HE THONG chua lam (sw-Q1 rao ③).
    """
    kh = " ".join(ht["kh"])
    nv = " ".join(ht["nv_noi"])
    t = TD["tc"]
    o = {}

    # TC-1 — phan hoi lan dau. Ngoai gio -> "—" + viec he thong.
    tg = trong_gio(ht["gio"])
    o["TC-1"] = "—" if tg is None or tg is False else ("✓" if nv else "✗")

    # TC-2 — hoi tinh trang TRUOC khi xin so
    o["TC-2"] = "✓" if chua(nv, t["TC-2_hoi_tinh_trang"]) else "✗"

    # TC-3 — ⛔ khong day sang kenh khac o luot dau
    dau = ht["nv_noi"][0] if ht["nv_noi"] else ""
    o["TC-3"] = "✗" if chua(dau, t["TC-3_day_kenh"]) else "✓"

    # TC-4 — goi dung rao khach mang
    rao = ht.get("rao") or ""
    ma_rao = {v: k for k, v in TEN_RAO.items()}.get(rao)
    o["TC-4"] = "—" if not ma_rao else ("✓" if chua(nv, TD["rao"][ma_rao]) else "✗")

    # TC-5 — tra loi bang co che/moc, ⛔ khong bang tinh tu tran an
    tinh_tu = ["very safe", "totally safe", "dont worry", "do not worry",
               "no problem", "its fine", "it is fine", "trust us", "very good"]
    if nv and chua(nv, tinh_tu):
        o["TC-5"] = "✗"                      # tran an bang tinh tu
    elif nv and chua(nv, t["TC-5_co_moc"]):
        o["TC-5"] = "✓"                      # co co che / moc cu the
    else:
        o["TC-5"] = "—"                      # ★ ⛔ KHONG cho ✓ mien phi

    # TC-6 — du kien an toan bat buoc, HAI danh sach
    khoa = "TC-6d_an_toan" if dong == "d" else "TC-6a_an_toan"
    o["TC-6"] = "✓" if chua(nv, t[khoa]) else "✗"

    # TC-7 — xac nhan khach den duoc (rang buoc MOT CO SO cua ban PH)
    o["TC-7"] = "✓" if (chua(nv, t["TC-7_den_duoc"]) or ht.get("vanh_dai") != "V0") else "✗"

    # TC-8 — ★ O DUY NHAT CONG DIEM CHO VIEC ⛔ KHONG TRA LOI (sw-Q1 §3)
    noi_se_hoi = chua(nv, TD["mien_tru"]["CD-S5"])
    tu_nghi_so = chua(nv, TD["co_do"]["CD-S5"]) and not noi_se_hoi
    o["_noi_se_hoi"] = noi_se_hoi
    if noi_se_hoi:
        o["TC-8"] = "✓"
    elif tu_nghi_so:
        o["TC-8"] = "✗"
    else:
        o["TC-8"] = "✓" if nv else "—"

    # TC-9 — cau cua rao quyet dinh. ★ Slot treo -> "—", ⛔ KHONG "✗".
    o["TC-9"] = "—" if slot_treo else ("✓" if chua(nv, TD["rao"]["LAU" if dong == "d" else "BEN"]) else "✗")

    # TC-10 — chot mot buoc tiep theo cu the
    o["TC-10"] = "✓" if chua(nv, t["TC-10_buoc_tiep"]) else "✗"

    # ★ an_toan = cap-tinh -> ⛔ KHONG cham cac o BAN (sw-Q1 §6)
    if ht.get("an_toan") == "cap-tinh":
        for k in ("TC-2", "TC-3", "TC-8", "TC-9", "TC-10"):
            o[k] = "—"
    return o


def diem_tc(o):
    co = sum(1 for v in o.values() if v == "✓")
    khong = sum(1 for v in o.values() if v == "✗")
    if co + khong == 0:
        return None, "—"
    pc = int(round(co * 100.0 / (co + khong)))
    loai = "A" if pc >= 85 else "B" if pc >= 70 else "C" if pc >= 50 else "D"
    return pc, loai


# ────────────────────────────────────────────────────────────────────
# 6 · CONG T — TAM CAU KIEM, CHAY BANG MAY  (sw-F §5)
# ────────────────────────────────────────────────────────────────────

CHAN_I = ["nv", "tc", "diem", "loai"]
CHAN_Q = ["cd", "hook", "ma_tran", "ads", "cau_hoi_ngam"]
RE_SDT = re.compile(r"(?<!\d)(?:\+?63|0)9\d{2}[\s.\-]?\d{3}[\s.\-]?\d{4}(?!\d)")
RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def _khoa(o, duong=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k), duong + "/" + str(k)
            for r in _khoa(v, duong + "/" + str(k)):
                yield r
    elif isinstance(o, list):
        for i, v in enumerate(o):
            for r in _khoa(v, duong + "[%d]" % i):
                yield r


def _chuoi(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            for r in _chuoi(v):
                yield r
    elif isinstance(o, list):
        for v in o:
            for r in _chuoi(v):
                yield r


def kiem_tuong_ngan(data, luong, ten_nv=None):
    """Tam cau cua CONG T. Tra ve list loi — rong la qua.

    ⚠ Chay BANG MAY, ⛔ khong bang mat. ghi_json() goi ham nay va TU CHOI GHI.
    """
    loi = []
    chuoi = list(_chuoi(data))

    # ── TUONG L ──
    # ① + ② + ③ — khoa bi chan theo luong
    chan = CHAN_I if luong == "insight" else CHAN_Q if luong == "qc" else []
    for k, duong in _khoa(data):
        if k in chan:
            loi.append("[%s] khoa bi chan '%s' tai %s" % (luong, k, duong))

    # ① — ten nhan vien that lot vao luong insight
    if luong == "insight" and ten_nv:
        for ten in ten_nv:
            ten = (ten or "").strip()
            if len(ten) < 3:
                continue
            for s in chuoi:
                if chuan(ten) and _re_cum(ten).search(chuan(s)):
                    loi.append("[insight] ten nhan vien '%s' lot vao: %s" % (ten, s[:80]))
                    break

    # ④ — file QC ⛔ khong chep ca hoi thoai
    if luong == "qc":
        for s in chuoi:
            if len(s) > 400:
                loi.append("[qc] trich khach qua dai (%d ky tu) — chi giu CAP CAU" % len(s))

    # ── TUONG D ──
    # ⑤ + ⑥ — moi ty le co NHAN DONG va mau so ⛔ khong tron
    for ty in _tim_ty_le(data):
        if ty.get("dong") not in ("a", "d", "ky"):
            loi.append("[tuong-D] ty le ⛔ khong co nhan dong: %s" % json.dumps(
                ty, ensure_ascii=False)[:120])
            continue
        mau = ty.get("mau")
        mong = (data.get("n") or {}).get(ty["dong"]) if ty["dong"] != "ky" \
            else data.get("tong_ht")
        if mau is not None and mong is not None and mau != mong:
            loi.append("[tuong-D] mau so tron: nhan '%s' nhung mau=%s, mong doi %s"
                       % (ty["dong"], mau, mong))

    # ── CHUNG ──
    # ⑦ — du lieu khach
    for s in chuoi:
        m = RE_SDT.search(s)
        if m:
            loi.append("[%s] so dien thoai: %s" % (luong, m.group(0)))
        m = RE_EMAIL.search(s)
        if m:
            loi.append("[%s] email: %s" % (luong, m.group(0)))

    # ⑧ — hai dong bat buoc
    if "tiếng Anh" not in (data.get("khai_mau") or ""):
        loi.append("[%s] thieu dong khai mau tieng Anh (sw-A §7)" % luong)
    if luong == "qc" and "kèm cặp" not in (data.get("chan_bang") or ""):
        loi.append("[qc] thieu cau chan bang")
    return loi


def _tim_ty_le(o):
    """Moi dict co khoa 'pc' duoc coi la mot ty le va phai co 'dong' + 'mau'."""
    if isinstance(o, dict):
        if "pc" in o:
            yield o
        for v in o.values():
            for r in _tim_ty_le(v):
                yield r
    elif isinstance(o, list):
        for v in o:
            for r in _tim_ty_le(v):
                yield r


def ghi_json(ten, data, luong=None, ten_nv=None):
    """⛔ Moi lan ghi JSON di qua day. ⛔ Khong goi json.dump o cho khac."""
    if luong:
        loi = kiem_tuong_ngan(data, luong, ten_nv)
        if loi:
            print("\n⛔ CỔNG T CHẶN — ⛔ KHÔNG ghi %s" % ten)
            for l in loi[:25]:
                print("   · " + l)
            if len(loi) > 25:
                print("   · … và %d lỗi nữa" % (len(loi) - 25))
            print("\n→ Sửa rồi chạy lại. Xem sw-F §5.")
            sys.exit(2)
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    p = os.path.join(OUT, ten)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    print("→ %s" % os.path.relpath(p, GOC))
    return p


def ty_le(tu, mau, dong):
    """★ Moi ty le mang NHAN DONG va MAU SO. ⛔ Khong tra ve mot so tran."""
    if not mau:
        return {"tu": tu, "mau": mau, "pc": None, "dong": dong, "ghi": "⏸ chưa đo được"}
    if mau < TD["nguong"]["mau_nhom"]:
        return {"tu": tu, "mau": mau, "pc": None, "dong": dong,
                "ghi": "⚠ n<10 — in số tuyệt đối, ⛔ không in phần trăm"}
    return {"tu": tu, "mau": mau, "pc": int(round(tu * 100.0 / mau)), "dong": dong}


# ────────────────────────────────────────────────────────────────────
# 7 · LENH  doc
# ────────────────────────────────────────────────────────────────────

def bang_ma_nv(ds):
    """Ten that -> NV-xx. ⛔ Bang quy doi KHONG vao file nao trong out/."""
    ten = sorted({h["nv"] for h in ds if h["nv"]})
    return {t: "NV-%02d" % (i + 1) for i, t in enumerate(ten)}


def lenh_doc(a):
    ds = doc_file(a.file)
    if not ds:
        print("⛔ Không đọc được hội thoại nào. Kiểm khuôn file — sw-B §3.")
        sys.exit(1)

    ma = bang_ma_nv(ds)
    goc = {"a": {"i": [], "q": []}, "d": {"i": [], "q": []}}
    cheo, chua_ro, v0 = [], [], 0

    for h in ds:
        kh = " ".join(h["kh"])
        dong_hoi = gan_dong_hoi(kh)
        vd = gan_vanh_dai(kh)
        if vd == "V0":
            v0 += 1
        nhom = gan_nhom(kh)
        lod = gan_lam_o_dau(kh)
        cap_bat_ky = bool(an_toan_bac(kh, "a") == "cap-tinh"
                          or an_toan_bac(kh, "d") == "cap-tinh")
        nhan = gan_nhan_ht(kh, lod, cap_bat_ky)
        co = soat_co_do(h["nv_noi"])

        for dong in dong_hoi:
            dv = gan_dv(kh, dong)
            chang = gan_chang(kh, dong)
            rao = gan_rao(kh, dong)
            at = an_toan_bac(kh, dong)
            bits = cham_bitmask(kh, dv)

            # ── nhanh i — ⛔ KHONG co nv / tc / diem / loai ──
            goc[dong]["i"].append({
                "ht": h["ht"], "ngay": h["ngay"], "kenh": h["kenh"],
                "dong_hoi": dong_hoi, "dv": dv, "chang": chang, "rao": rao,
                "vanh_dai": vd, "nhom": nhom, "lam_o_dau": lod,
                "nhan_ht": nhan, "an_toan": at,
                "luot_kh": len(h["kh"]), "ngan": len(h["kh"]) <= 2,
                "bits": bits, "do_nong": sum(bits),
                "trich_khach": h["kh"][:3],
                "post_ads": h["post_ads"],
                "co_do_dem": sorted({c[0] for c in co}),
            })

            # ── nhanh q — ⛔ KHONG co cd / hook / cau_hoi_ngam ──
            if h["nv"]:
                ctx = dict(rao=rao, vanh_dai=vd, an_toan=at)
                ht_ctx = dict(h, **ctx)
                o = cham_tc(ht_ctx, dong)
                se_hoi = bool(o.pop("_noi_se_hoi", False))
                pc, loai = diem_tc(o)
                goc[dong]["q"].append({
                    "ht": h["ht"], "nv": ma[h["nv"]], "dong_hoi": dong_hoi,
                    "dv": dv, "vanh_dai": vd, "nhom": nhom,
                    "lam_o_dau": lod, "nhan_ht": nhan, "an_toan": at,
                    "noi_se_hoi": se_hoi,
                    "tc": o, "diem": pc, "loai": loai,
                    "co_do": [{"ma": c[0], "cau": c[1]} for c in co],
                    "bang_chung": h["kh"][:1] + h["nv_noi"][:1],
                })

        if not dong_hoi:
            # ★ ⛔ KHONG doan dong. Doan la pha chinh TUONG D: mot hoi thoai
            #   bi gan sai dong se vao MAU SO cua dong do.
            chua_ro.append({"ht": h["ht"], "trich": h["kh"][:1]})
        if len(dong_hoi) > 1:
            cheo.append({"ht": h["ht"],
                         "vao_bang": (gan_dv(kh, dong_hoi[0]) or [""])[0],
                         "hoi_sang": dong_hoi[1]})

    tong = len(ds)
    nguong = TD["nguong"]["v0_cong_g"]
    qua_g = (v0 / float(tong)) < nguong if tong else False

    data = {
        "ky": a.ky, "doc_luc": a.ky and None or None,
        "ngon_ngu_mau": ["en"],
        "chua_doc_duoc": ["taglish", "fil", "ko", "fa"],
        "khai_mau": CAU_MAU,
        "tong_ht": tong,
        "n": {"a": len(goc["a"]["i"]), "d": len(goc["d"]["i"]),
              "cheo": len(cheo), "ky": tong},
        "cong_g": {"v0": v0, "v0_pc": int(round(v0 * 100.0 / tong)) if tong else 0,
                   "nguong_pc": int(nguong * 100), "qua": qua_g},
        "a": goc["a"], "d": goc["d"], "cheo": cheo,
        "chua_ro_dong": {
            "n": len(chua_ro), "ht": chua_ro,
            "ghi": ("★ ⛔ KHÔNG đoán dòng — như V0. Hội thoại ⛔ không có dấu "
                    "hiệu dòng nào thì ⛔ không vào phễu của dòng nào, vì vào "
                    "sai dòng là vào sai MẪU SỐ (tường D)."),
        },
    }
    data.pop("doc_luc")

    # ⛔ File goc chua nhanh q -> ⛔ KHONG chay CONG T theo luong, va
    #    ⛔ KHONG publish. Luat o sw-D §4.
    ghi_json("doc-hoi-thoai.json", data)

    print("\n★ ĐỌC — kỳ %s" % a.ky)
    print("   tổng HT phân biệt : %d   ⚠ ⛔ KHÔNG bằng n(a)+n(d)" % tong)
    print("   dòng a (thẩm mỹ)  : %d" % data["n"]["a"])
    print("   dòng d (nha khoa) : %d" % data["n"]["d"])
    print("   ★ chéo (cả hai)   : %d" % data["n"]["cheo"])
    print("   ⏸ ⛔ chưa rõ dòng : %d   ★ ⛔ KHÔNG đoán — xem chua_ro_dong"
          % data["chua_ro_dong"]["n"])
    print("   nhân viên          : %d → NV-01…NV-%02d" % (len(ma), len(ma)))
    g = data["cong_g"]
    print("\n%s CỔNG G — V0 = %d/%d (%d%%), ngưỡng %d%%"
          % ("✅" if g["qua"] else "⛔", g["v0"], tong, g["v0_pc"], g["nguong_pc"]))
    if not g["qua"]:
        print("   ⛔ DỪNG — ⛔ không kết luận theo vành đai. Hỏi người. (sw-A §5)")
    print("\n⚠ %s" % CAU_MAU)


# ────────────────────────────────────────────────────────────────────
# 8 · LENH  insight
# ────────────────────────────────────────────────────────────────────

def nap_goc():
    p = os.path.join(OUT, "doc-hoi-thoai.json")
    if not os.path.isfile(p):
        print("⛔ Chưa có out/doc-hoi-thoai.json. Chạy `doc` trước.")
        sys.exit(1)
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def _dem(ds, lay):
    d = {}
    for h in ds:
        v = lay(h)
        for x in (v if isinstance(v, list) else [v]):
            if x:
                d[x] = d.get(x, 0) + 1
    return dict(sorted(d.items(), key=lambda kv: -kv[1]))


def _hot(ds, lay, truc):
    """★ Bang do nong BUOC PHAI co cot HOT* (sw-I2 §3)."""
    nhom = {}
    for h in ds:
        v = lay(h)
        for x in (v if isinstance(v, list) else [v]):
            if not x:
                continue
            nhom.setdefault(x, []).append(h)
    bo = BO_BIT[truc]
    ra = []
    for k, hs in nhom.items():
        n = len(hs)
        ra.append({
            "nhom": k, "n": n,
            "hot": round(sum(h["do_nong"] for h in hs) / float(n), 1),
            "hot_sao": round(sum(hot_sao(h["bits"], bo) for h in hs) / float(n), 1),
            "bo_bit": sorted(bo),
        })
    for r in ra:
        r["chenh"] = round(r["hot"] - r["hot_sao"], 1)
    return sorted(ra, key=lambda r: -r["hot_sao"])


def lenh_insight(a):
    goc = nap_goc()
    dong = a.dong
    ds = goc[dong]["i"]
    n = len(ds)
    if not n:
        print("⛔ Dòng %s ⛔ không có hội thoại nào." % dong)
        sys.exit(1)

    ngan = [h for h in ds if h["ngan"]]
    data = {
        "ky": goc["ky"], "dong": dong, "n": {dong: n, "ky": goc["tong_ht"]},
        "tong_ht": goc["tong_ht"], "khai_mau": goc["khai_mau"],
        "cong_g": goc["cong_g"],
        "cong_0": "⏸ CHƯA DUYỆT — chân dung nhãn PHÁC. ⛔ Không viết hook.",
        "chang": _dem(ds, lambda h: h["chang"]),
        "rao": _dem(ds, lambda h: h["rao"]),
        "dv": _dem(ds, lambda h: h["dv"]),
        "vanh_dai": _dem(ds, lambda h: h["vanh_dai"]),
        "nhom": _dem(ds, lambda h: h["nhom"]),
        "lam_o_dau": _dem(ds, lambda h: h["lam_o_dau"]),
        "an_toan": _dem(ds, lambda h: h["an_toan"]),
        "hot_theo_dv": _hot(ds, lambda h: h["dv"], "dv"),
        "hot_theo_chang": _hot(ds, lambda h: h["chang"], "chang"),
        "hot_theo_vanh_dai": _hot(ds, lambda h: h["vanh_dai"], "vanh_dai"),
        "ht_ngan": {
            "ty_le": ty_le(len(ngan), n, dong),
            "cau_hoi_dau": [h["trich_khach"][0] for h in ngan if h["trich_khach"]][:10],
            "ghi": "★ Nhóm đông nhất và ⛔ hay bị bỏ qua nhất — sw-I1 §6 ③",
        },
        "phan_anh": [h["ht"] for h in ds if h["nhan_ht"] == "phan-anh"],
        "quay_lai": {
            "ht": [h["ht"] for h in ds if h["nhan_ht"] == "quay-lai"],
            "ghi": ("★ Khách QUAY LẠI — ⛔ KHÔNG phải phản ánh. Đây là tài sản "
                    "của cơ sở hai dòng, đọc cùng ô `cheo` — sw-C §4."),
        },
        "cap_tinh": [h["ht"] for h in ds if h["an_toan"] == "cap-tinh"],
        "co_do_dem": _dem(ds, lambda h: h["co_do_dem"]),
        "cheo": {"ty_le": ty_le(goc["n"]["cheo"], goc["tong_ht"], "ky"),
                 "ghi": "★ Mẫu số là TỔNG KỲ, ⛔ không phải n của một dòng — sw-F §2"},
    }
    ghi_json("insight-%s.json" % dong, data, luong="insight",
             ten_nv=None)

    print("\n★ INSIGHT — dòng %s · kỳ %s · n=%d (tổng kỳ %d)"
          % (dong, goc["ky"], n, goc["tong_ht"]))
    print("\n%-22s %s" % ("CHẶNG", data["chang"]))
    print("%-22s %s" % ("RÀO", data["rao"]))
    print("%-22s %s" % ("VÀNH ĐAI", data["vanh_dai"]))
    print("\n★ ĐỘ NÓNG theo DV — cột HOT* là cột đáng tin:")
    print("   %-10s %4s %6s %7s %7s" % ("nhóm", "n", "HOT", "HOT*", "chênh"))
    for r in data["hot_theo_dv"][:8]:
        print("   %-10s %4d %6.1f %7.1f %7.1f"
              % (r["nhom"], r["n"], r["hot"], r["hot_sao"], r["chenh"]))
    print("\n⏸ %s" % data["cong_0"])
    if data["phan_anh"]:
        print("⚠ %d hội thoại PHẢN ÁNH (làm tại Sunwoo + có dấu hiệu vấn đề) "
              "→ mục riêng: %s"
              % (len(data["phan_anh"]), ", ".join(data["phan_anh"])))
    if data["quay_lai"]["ht"]:
        print("★ %d hội thoại KHÁCH QUAY LẠI (⛔ không phải phản ánh): %s"
              % (len(data["quay_lai"]["ht"]), ", ".join(data["quay_lai"]["ht"])))
    if data["cap_tinh"]:
        print("🔴 %d hội thoại CẤP TÍNH → ⛔ không bán: %s"
              % (len(data["cap_tinh"]), ", ".join(data["cap_tinh"])))
    print("\n⚠ %s" % goc["khai_mau"])


# ────────────────────────────────────────────────────────────────────
# 9 · LENH  qc
# ────────────────────────────────────────────────────────────────────

def lenh_qc(a):
    goc = nap_goc()
    dong = a.dong
    ds = goc[dong]["q"]
    n = len(ds)
    if not n:
        print("⛔ Dòng %s ⛔ không có hội thoại nào có nv." % dong)
        sys.exit(1)

    nguoi = {}
    for h in ds:
        nguoi.setdefault(h["nv"], []).append(h)

    bang = []
    for nv, hs in sorted(nguoi.items()):
        mong = len(hs)
        co = sum(1 for h in hs for v in h["tc"].values() if v == "✓")
        khong = sum(1 for h in hs for v in h["tc"].values() if v == "✗")
        gach = sum(1 for h in hs for v in h["tc"].values() if v == "—")
        pc = int(round(co * 100.0 / (co + khong))) if co + khong else None
        du = mong >= TD["nguong"]["mau_nguoi"]
        bang.append({
            "nv": nv, "dong": dong, "n": mong,
            "co": co, "khong": khong, "gach": gach,
            "pc": pc if du else None,
            "loai": (("A" if pc >= 85 else "B" if pc >= 70 else "C" if pc >= 50
                      else "D") if (du and pc is not None) else "—"),
            "ghi": "" if du else "⚠ MỎNG n<10 — in số thật, ⛔ KHÔNG gán loại",
        })

    o_gach = {}
    for h in ds:
        for k, v in h["tc"].items():
            if v == "—":
                o_gach[k] = o_gach.get(k, 0) + 1

    co_do = {}
    for h in ds:
        for c in h["co_do"]:
            co_do.setdefault(c["ma"], []).append(h["ht"])

    data = {
        "ky": goc["ky"], "dong": dong, "n": {dong: n, "ky": goc["tong_ht"]},
        "tong_ht": goc["tong_ht"], "khai_mau": goc["khai_mau"],
        "chan_bang": CHAN_BANG,
        "bang_nguoi": bang,
        "o_gach": o_gach,
        "co_do": {k: {"luot": len(v), "ht": v} for k, v in co_do.items()},
        "lam_dung_se_hoi": sum(1 for h in ds if h.get("noi_se_hoi")),
        "viec_he_thong": [
            {"viec": "Khoảng tháng cắm → răng cuối theo từng DV-D*",
             "ai_cap": "Bác sĩ", "chan": "TC-9 toàn khối · chặng SD4"},
            {"viec": "T&C bảo hành bằng văn bản",
             "ai_cap": "Pháp chế", "chan": "NGỜ② · site đang hứa mà ⛔ chưa có văn bản"},
            {"viec": "Có nhận HMO nào không",
             "ai_cap": "Vận hành", "chan": "toàn bộ nhóm N2 dòng d"},
            {"viec": "Hướng dẫn chuyển dòng a ↔ d",
             "ai_cap": "Vận hành", "chan": "cờ CĐ-S4 — ⛔ chưa có thì ⛔ không phải lỗi người"},
        ],
        "ghi": ("★ Kỳ đầu: TC-9 gần như luôn '—'. Mục việc hệ thống DÀI HƠN "
                "phần chấm điểm là dấu hiệu bảng chấm ĐANG CHẠY ĐÚNG — sw-Q1 §5."),
    }
    ghi_json("qc-%s.json" % dong, data, luong="qc")

    print("\n★ QC — dòng %s · kỳ %s · n=%d" % (dong, goc["ky"], n))
    print("\n   %-7s %4s %4s %4s %4s %6s %5s  %s"
          % ("NV", "n", "✓", "✗", "—", "%", "loại", "ghi"))
    for b in bang:
        print("   %-7s %4d %4d %4d %4d %6s %5s  %s"
              % (b["nv"], b["n"], b["co"], b["khong"], b["gach"],
                 b["pc"] if b["pc"] is not None else "—", b["loai"], b["ghi"]))
    print("\n★ Ô '—' theo tiêu chí (⛔ KHÔNG vào mẫu số): %s" % o_gach)
    print("★ Số lượt nhân viên chọn cách ĐÚNG ('let me confirm'): %d"
          % data["lam_dung_se_hoi"])
    if co_do:
        print("\n⚠ CỜ ĐỎ:")
        for k, v in sorted(co_do.items()):
            print("   %-8s %d lượt — %s" % (k, len(v), ", ".join(v[:6])))
    else:
        print("\n✅ ⛔ Không cờ đỏ nào (miễn trừ đã xét trước — sw-Q2 §1)")
    print("\n%s" % CHAN_BANG)


# ────────────────────────────────────────────────────────────────────
# 10 · LENH  kiem
# ────────────────────────────────────────────────────────────────────

def lenh_kiem(a):
    with io.open(a.file, encoding="utf-8") as f:
        data = json.load(f)
    luong = "insight" if "insight" in os.path.basename(a.file) else \
            "qc" if "qc" in os.path.basename(a.file) else None
    if luong is None:
        print("⛔ ⛔ Không suy được luồng từ tên file. Đặt tên có 'insight' hoặc 'qc'.")
        sys.exit(1)
    ten = None
    if a.ma_nv and os.path.isfile(a.ma_nv):
        with io.open(a.ma_nv, encoding="utf-8") as f:
            ten = [l.split(",")[0].strip() for l in f if l.strip()]
    loi = kiem_tuong_ngan(data, luong, ten)
    if loi:
        print("⛔ CỔNG T TRƯỢT — %d lỗi:" % len(loi))
        for l in loi:
            print("   · " + l)
        sys.exit(2)
    print("✅ CỔNG T qua — %s (luồng %s)" % (os.path.basename(a.file), luong))


# ────────────────────────────────────────────────────────────────────

def main():
    nap_tu_dien()
    p = argparse.ArgumentParser(prog="sw.py", description="Insight Dashboard Sunwoo")
    s = p.add_subparsers(dest="lenh")

    d = s.add_parser("doc", help="đọc hội thoại → out/doc-hoi-thoai.json")
    d.add_argument("file")
    d.add_argument("--ky", required=True)
    d.set_defaults(f=lenh_doc)

    i = s.add_parser("insight", help="luồng I, một dòng")
    i.add_argument("--dong", required=True, choices=["a", "d"])
    i.set_defaults(f=lenh_insight)

    q = s.add_parser("qc", help="luồng Q, một dòng")
    q.add_argument("--dong", required=True, choices=["a", "d"])
    q.set_defaults(f=lenh_qc)

    k = s.add_parser("kiem", help="chạy CỔNG T trên một file JSON")
    k.add_argument("file")
    k.add_argument("--ma-nv", dest="ma_nv", default=os.path.join(GOC, "ma-nhan-vien.csv"))
    k.set_defaults(f=lenh_kiem)

    a = p.parse_args()
    if not getattr(a, "f", None):
        p.print_help()
        sys.exit(1)
    a.f(a)


if __name__ == "__main__":
    main()
