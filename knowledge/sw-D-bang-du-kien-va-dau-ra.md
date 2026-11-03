# sw-D · BẢNG DỮ KIỆN GỐC & ĐẦU RA

> Sổ này là **hợp đồng dữ liệu** của repo. Mọi lệnh đọc cùng một bảng, mọi báo cáo đọc lại từ cùng một file — nên ⛔ **không bao giờ lệch số**.

---

## 1. MỘT LẦN ĐỌC → MỘT BẢNG

```
hội thoại  →  tools/sw.py doc  →  out/doc-hoi-thoai.json
                                      │
                   ┌──────────────────┴──────────────────┐
              INSIGHT (--dong a|d)                  QC (--dong a|d)
                   │                                     │
            out/insight-<dong>.json              out/qc-<dong>.json
            out/dashboard-i-<dong>.html          out/dashboard-q-<dong>.html
                   │                                     │
            ✅ publish được sau CỔNG T          ⛔ KHÔNG publish
```

⛔ **Không đọc lại hội thoại ở bước thứ hai.** Hai lần đọc là hai bộ số, và hai bộ số lệch nhau là thứ phá hỏng một báo cáo nhanh hơn mọi lỗi khác.

---

## 2. CỘT CỦA BẢNG GỐC

| Cột | Kiểu | Nghĩa | Vào nhánh |
|---|---|---|---|
| `ht` | `"HT-001"` | ★ Khoá duy nhất | **cả hai** |
| `ngay` · `gio` | `"2026-11-04"` · `"10:12"` | Mốc để chấm `TC-1` | cả hai |
| `kenh` | `messenger`·`instagram`·`viber`·`whatsapp` | Kênh | cả hai |
| ★ `dong_hoi` | **list** `["a"]`·`["d"]`·`["a","d"]` | ★ **Dòng khách hỏi** — là **danh sách** | cả hai |
| `dv` | list `DV-A1`…`DV-D7`·`DV-A0`·`DV-D0` | Dịch vụ khách nhắc | cả hai |
| `chang` | `S1`…`S6` *(dòng `a`)* · `SD1`…`SD6` *(dòng `d`)* | Chặng phễu | `i` |
| `rao` | `SỢ`·`NGỜ`·`NGẠI`·`BỀN`·`LÂU` | Rào nặng nhất | `i` · 🔶 `q` |
| `vanh_dai` | `V0`…`V4` | Vành đai | cả hai |
| `nhom` | `N1`·`N2`·`N3`·`""` | Nhóm đặc thù | cả hai |
| `cd` | `CD1`…`CD6` · `CD-D1`…`CD-D6` | Chân dung | ⛔ **chỉ `i`** |
| `lam_o_dau` | `tai-sunwoo`·`noi-khac`·`""` | ★ Dữ kiện **độc lập** | cả hai |
| `an_toan` | `cap-tinh`·`can-bs`·`""` | ★ **Hai bậc** | cả hai |
| `cau_hoi_ngam` | string | Câu khách thật sự muốn hỏi | `i` |
| `trich_khach` | list | Nguyên văn, **đã ẩn danh** | `i` · 🔶 `q` |
| `post_ads` | string | Nhãn nguồn vào | `i` |
| `loi_he` | list | Việc hệ thống | **cả hai** |
| **`nv`** | `"NV-04"` | Nhân viên | ⛔ **chỉ `q`** |
| `tc` | dict `{1..10}` → `✓`/`✗`/`—` | Mười ô chấm | ⛔ **chỉ `q`** |
| `diem` · `loai` | int · `A`/`B`/`C`/`D` | Điểm & phân loại | ⛔ **chỉ `q`** |
| `co_do` | list `CĐ-S1`…`CĐ-S10` | Cờ đỏ | `q` đầy đủ · 🔶 `i` đếm tổng |

### ★ Vì sao `dong_hoi` là **danh sách** chứ ⛔ không phải một giá trị

Một hội thoại hỏi *"how much for veneers?"* rồi ba tin sau hỏi *"do you also do melasma?"* là **một dữ kiện ⛔ không dòng nào tự thấy được**. Nếu `dong_hoi` là một giá trị thì phải chọn — và chọn thì **mất nửa dữ kiện**.

### ★ Vì sao `an_toan` có **ba** giá trị chứ ⛔ không phải hai

Xem `sw-C` §5. Tóm: `"does it hurt?"` là câu hỏi **bán hàng bình thường** của chặng `SD3`; `"my face is swelling and I have a fever"` là **cấp cứu**. Một bậc duy nhất thì hoặc bỏ sót ca cấp cứu, hoặc **miễn chấm oan** một ca tư vấn tốt — và cái thứ hai là **mất phần khen đúng**.

---

## 3. CẤU TRÚC FILE GỐC

```json
{
  "ky": "28/10-03/11",
  "doc_luc": "2026-11-03T14:20",
  "ngon_ngu_mau": ["en"],
  "chua_doc_duoc": ["taglish", "fil", "ko", "fa"],
  "tong_ht": 73,
  "n": { "a": 52, "d": 21, "cheo": 6 },
  "cong_g": { "v0": 9, "v0_pc": 12, "qua": true },

  "a": {
    "i": [ { "ht": "HT-001", "chang": "S4", "rao": "BỀN", … } ],
    "q": [ { "ht": "HT-001", "nv": "NV-04", "tc": {…}, … } ]
  },
  "d": {
    "i": [ … ],
    "q": [ … ]
  },
  "cheo": [ { "ht": "HT-017", "vao_bang": "DV-D7", "hoi_sang": "DV-A5" } ]
}
```

> ⚠️ **`tong_ht` ⛔ KHÔNG bằng `n.a + n.d`.**
> `52 + 21 = 73` ở ví dụ trên là **trùng hợp của số liệu mẫu** — nói chung `n.a + n.d = tong_ht + n.cheo`, vì hội thoại chéo nằm trong **cả hai** nhánh.
>
> ★ `tong_ht` = **số `ht` phân biệt**. Mọi tỷ lệ nhãn `ky` lấy mẫu số này.

### Ô `cheo` — ba luật

```
① Hội thoại chéo vào phễu CỦA CẢ HAI dòng (vì khách thật sự hỏi cả hai).
② Vào list `cheo` ĐÚNG MỘT LẦN.
③ Tỷ lệ chéo lấy mẫu số `tong_ht`, ⛔ KHÔNG phải n của một dòng.
   ★ Lấy mẫu số một dòng thì CÙNG MỘT dữ kiện ra HAI tỷ lệ khác nhau,
     và cả hai đều trông hợp lý. Xem sw-F §2.
```

★ `vao_bang` = dịch vụ **khách hỏi trước**. Đây là cột làm cho ô `cheo` **dùng được**: biết `DV-D7 General Dentistry` là cửa vào thì biết nên đặt nội dung chéo ở đâu.

---

## 4. ĐẦU RA — SÁU FILE, HAI NHÓM QUYỀN

| File | Nhánh | Publish? | Người nhận |
|---|---|---|---|
| `out/doc-hoi-thoai.json` | gốc | ⛔ **Không** — chứa cả `nv` | ⛔ Không ai, chỉ máy đọc |
| `out/insight-a.json` · `-d.json` | `i` | ✅ sau CỔNG T | Marketing |
| `out/dashboard-i-a.html` · `-d.html` | `i` | ✅ sau CỔNG T | Marketing |
| `out/qc-a.json` · `-d.json` | `q` | ⛔ **Không** | Trưởng nhóm |
| `out/dashboard-q-a.html` · `-d.html` | `q` | ⛔ **Không** | Trưởng nhóm |
| `out/so-tay-NV-xx.md` | `q` | ⛔ **Không** | ⛔ **Chỉ người đó** |

> ⚠️ **File gốc ⛔ không được publish, dù nó trông như file trung gian vô hại.** Nó chứa nhánh `q`, tức là chứa `nv` — và nó là file **dễ bị gửi đi nhất** vì tên nó nghe như một file tạm.

★ **Luật đặt tên:** mọi file mang nhánh `q` có chữ `qc` hoặc `so-tay` trong tên. ⛔ Không đặt tên trung tính cho file có tên người.

---

## 5. DASHBOARD — HAI CÁI, HAI LUẬT

| | **Dashboard `i`** | **Dashboard `q`** |
|---|---|---|
| Nội dung | Chân dung · chặng · rào · `DV-*` · ô `cheo` · cờ đỏ **đếm tổng** | `NV-xx` · mười ô `TC` · điểm · cờ đỏ **đầy đủ** |
| Có tên người? | ⛔ **Không** | ✅ `NV-xx` |
| Publish ra link? | ✅ **được** | ⛔ **Không bao giờ** |
| Câu chân bảng | ⬜ | ★ **bắt buộc** |

★ **Cả hai dashboard phải in `tong_ht` và `n` của dòng ở đầu trang**, cạnh mọi tỷ lệ. Một dashboard có phần trăm mà ⛔ không có mẫu số là một dashboard **⛔ không đọc được** — `67%` của 3 hội thoại và `67%` của 300 hội thoại trông giống nhau trên biểu đồ.

★ **Và cả hai phải in dòng khai mẫu** *(`sw-A` §7)*: mẫu chỉ gồm tiếng Anh.

---

## 6. ⛔ BA ĐIỀU ĐẦU RA ⛔ KHÔNG ĐƯỢC CÓ

```
① ⛔ KHÔNG có một con số tổng cho cả cơ sở.
   ★ Đưa HAI con số kèm hai mẫu số. Xem sw-F §8 ④.

② ⛔ KHÔNG có phần trăm khi n < 10.
   In số tuyệt đối. "2/3" trung thực hơn "67%".

③ ⛔ KHÔNG có ô nào điền giá trị mặc định cho đẹp bảng.
   Thiếu dữ kiện → "—" + LÝ DO. Một ô "—" có lý do thì người đọc
   biết phải cấp gì; một ô đã điền sai thì ⛔ không ai biết.
```

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] `tong_ht` có bị tính bằng `n.a + n.d` không? *(⛔ sai — phải là số `ht` phân biệt)*
- [ ] Hội thoại chéo có vào list `cheo` **đúng một lần** chưa?
- [ ] File nào mang nhánh `q` mà **tên ⛔ không có** `qc`/`so-tay` không?
- [ ] `out/doc-hoi-thoai.json` có bị đưa vào thứ gì sắp gửi đi không?
- [ ] Dashboard có in `tong_ht` + `n` của dòng cạnh mọi tỷ lệ chưa?
- [ ] Có phần trăm nào in khi `n < 10` không?
- [ ] Dashboard `q` có bị publish ra link không?
