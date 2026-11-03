# Agent · Đọc Insight khách — Sunwoo Medical Center 🇵🇭

> Đọc **hội thoại khách nhắn vào** của **Sunwoo Medical Center** *(Ground floor, 20 Upper McKinley Hill, Taguig, Metro Manila)* và trả hai thứ cho hai người khác nhau, trên **hai dòng dịch vụ**.

`v1.0` · 03/11/2026 · **Philippines** · hai dòng: [sunwooaesthetic.ph](https://sunwooaesthetic.ph/) · [sunwoodental.ph](https://sunwoodental.ph/)

---

## ★★ Một lần đọc · hai dòng · hai tường

```
MỘT lần đọc  →  out/doc-hoi-thoai.json
   ├── a/  dòng THẨM MỸ   ──┬── i/  insight khách  → Marketing
   │                         └── q/  QC trực page   → trưởng nhóm
   └── d/  dòng NHA KHOA  ──┬── i/
                             └── q/
```

| | **TƯỜNG D** *(dòng)* | **TƯỜNG L** *(luồng)* |
|---|---|---|
| Chặn gì | ⛔ Không **tỷ lệ** nào có mẫu số trộn `a` + `d` | ⛔ Không **file** nào có cả tên nhân viên và lời khách |
| Đơn vị bị chặn | **Phép chia** | **Trường dữ liệu** |
| Vi phạm nghĩa là | Một con số trông hợp lý mà ⛔ **không nói về ai cả** | Một **con người** bị nêu tên trong file ⛔ không dành cho họ |

★ **Hai tường CỘNG vào nhau, ⛔ không nhân lên.** Tường L chặn **chỗ đặt dữ liệu**; tường D chặn **phép tính**. Nên cấu trúc chỉ cần lồng **một lần** — xem [`sw-A`](knowledge/sw-A-vai-tro-hai-tuong.md) §3.

---

## ⛔ Việc agent này ⛔ không làm

| Việc | Của ai |
|---|---|
| Nghiên cứu từ khoá · mẫu quảng cáo · landing · chẩn đoán chỉ số ads | ★ [`Agent-AdsOptimize-Phi`](../Agent-AdsOptimize-Phi/) |
| Duyệt pháp chế câu chữ ở PH | **Pháp chế phòng khám** — agent chỉ **rà và đánh dấu** |
| Duyệt chuyên môn y khoa / nha khoa | **Bác sĩ** |
| Quyết định nhân sự · kỷ luật · xếp hạng công khai | ⛔ **Không ai** |
| Trả lời khách · sửa CRM | ⛔ **Không agent nào** |

### ★★ Luật sổ nhập — **sổ ngoài thắng**

`Agent-AdsOptimize-Phi` **đã có bốn sổ** về chính thương hiệu này và chính thị trường này. Repo này **nhập**, ⛔ **không viết lại**, và khi mâu thuẫn thì **sổ đó thắng**:

| Sổ nhập | Chứa gì |
|---|---|
| `kn-ho-so-thuong-hieu-sunwoo.md` | 6 dịch vụ dòng `a` · 2 bác sĩ · con số site · ★ **6 lỗi production** · 10 slot |
| `kn-vung-philippines.md` | ★ **bốn vành đai `V1`–`V4`** · nhóm `N1`–`N3` · ngôn ngữ · kênh · tiền tệ · mùa vụ |
| `kn-rao-phap-ly-ph.md` | hai tầng rào · ★ **checklist 12 ô** · bảng từ cấm · `RA 10173` · ba cửa duyệt |
| `kn-chan-dung-hanh-trinh-ph.md` | ★ **phễu `S1`–`S6`** · rào `SỢ·NGỜ·NGẠI·BỀN` · `CD1`–`CD6` |

> ⛔ **Không nạp tri thức của `Agent-InsightDashboard-Kangnam` · `-Paris` · `-KNQT` vào cùng project.** Bộ mã khác, luật hiển thị giá khác, và **luật của một nước khác** *(Việt Nam `91/2025/QH15`)*. Ở đây là **Philippines `RA 10173`**.

---

## ★★ Hai dòng khác nhau ở **quyết định mua**, ⛔ không ở dịch vụ

| | `a` **THẨM MỸ** | `d` **NHA KHOA** |
|---|---|---|
| Hình tiền | Nhiều lần nhỏ, **lặp lại** | ★ **Một lần lớn**, ⛔ không lặp |
| Hình thời gian | Buổi cách nhau vài tuần | ★ **Nhiều tháng** — chờ xương liền |
| Kết quả | **Có thời hạn** | Vĩnh viễn hoặc gần vĩnh viễn |
| Câu hỏi khoá | *"Năm sau còn phải trả bao nhiêu?"* | *"Bao lâu thì tôi có răng?"* |
| Rào thứ tư | **`BỀN`** | ★ **`LÂU`** |
| Chặng quyết định | **`S4`** số buổi & tổng chi phí | ★ **`SD4`** thời gian & số lần hẹn |

```
⛔ Một con số trộn hai dòng ⛔ KHÔNG nói về ai:

"Tỷ lệ khách hỏi giá rồi im = 44%"
  dòng a: khách tính ra 6 buổi × ₱X  → sửa bằng BẢNG LIỆU TRÌNH (nội dung)
  dòng d: khách nghe tổng All-on-4    → sửa bằng TRẢ GÓP / HMO  (chính sách)

★ Một con số, HAI việc khác nhau hoàn toàn. Và người đọc sẽ chọn MỘT —
  thường là việc của dòng đông hơn.
```

★ **`NGỜ` của dòng `d` xuất hiện HAI lần**, và lần thứ hai ở `SD6` mới là lần **mất ca đắt nhất**: khách đã chấp nhận giá rồi mới hỏi *"hãng nào, ai cắm, bảo hành ra sao"*. Chi tiết: [`sw-C`](knowledge/sw-C-hai-dong-hai-phe-u.md).

---

## Bốn cổng chặn

| Cổng | Chặn gì | Máy chạy? |
|---|---|---|
| **CỔNG 0** | ⛔ Chưa duyệt chân dung → ⛔ không viết hook, ⛔ không ra việc | ⬜ |
| ★ **CỔNG G** | `V0` ≥ 20% mẫu → ⛔ **DỪNG**, ⛔ không kết luận theo vành đai | ✅ |
| **CỔNG 2** | ⛔ Chưa rà pháp lý PH → ⛔ không xuất bản chạy được | 🔶 |
| ★★ **CỔNG T** | Trượt tường → **từ chối ghi file** `sys.exit(2)` | ✅ |

### ★ CỔNG G — cổng riêng của bản Philippines

Phòng khám có **một cơ sở** và khách phải **đến tận nơi**. Một kết luận *"nhóm này chốt kém"* mà ⛔ không biết họ ở đâu **có thể chỉ là** *"họ ở Quezon City và ⛔ không ai vượt EDSA 70 phút để trị nám một buổi"* — hai việc đó cần **hai cách sửa khác nhau**.

⚠️ Trường `Your area` trên **cả hai** form đang là **ô text tự do**, nên vành đai phần lớn phải **suy từ lời khách** — và suy thì sai được. Vì vậy **`V0` là một giá trị thật**, ⛔ không phải một ô rỗng cần điền cho đủ.

---

## ★ Site đang công bố câu ⛔ không dùng được

**Phát hiện quan trọng nhất của repo:** hai câu **mạnh nhất** trên site nha khoa trả lời **đúng hai rào quyết định** — và ⛔ **cả hai ⛔ không dùng được như đang viết**:

| Câu trên site | Trả lời rào | Vướng |
|---|---|---|
| *"2× faster bone integration"* | ★ **`LÂU`** — rào quyết định `SD4` | Ô ④ — thiếu nguồn và thiếu *"nhanh hơn cái gì"* |
| *"written warranty"* | ★ **`NGỜ`②** — rào mất ca đắt nhất | Ô ② — cam kết **kết quả** |

★ Nghĩa là cơ sở **cược đúng chỗ**; vấn đề là **claim chưa có hồ sơ chống lưng**. Việc đáng làm ⛔ **không phải xoá hai câu đó**, mà là **làm cho chúng dùng được** — thay `"2×"` bằng **khoảng tháng thật**, thay *"warranty"* bằng **care plan có T&C**.

✅ **Dùng được ngay, và site đang để chìm:** ★ **`Dr. Kay Dela Cruz`, D.M.D., cắm implant từ 1999 — hơn 25 năm** · `Dr. Shilan`, D.D.M., ORIS · **English · Tagalog · Farsi** · **Mon–Sun 9AM–6PM** · **Ground floor** · free consultation · private suites.

> ★ Ở một thị trường mà câu ngầm là *"năm năm nữa nó lung lay thì ai chịu"*, **một con số năm hành nghề** là bằng chứng mạnh hơn mọi tính từ — và nó ⛔ **không cần ô dữ liệu nào mới**.

Chi tiết: [`sw-G`](knowledge/sw-G-phap-ly-ph-cho-bao-cao.md).

---

## Ngôn ngữ — English, và ⚠️ điều đó **có giá**

Bản này đọc **tiếng Anh**. Bỏ ba thứ tiếng còn lại ⛔ **không trung tính** — nó **lệch mẫu theo đúng những nhóm đáng chú ý nhất**:

| ⏸ Chưa đọc được | Mất nhóm nào | Hệ quả thật |
|---|---|---|
| **Taglish** | Nhóm **Messenger** — kênh số 1 ở PH | *"magkano po ang thread lift"* ⛔ không khớp `price` → hội thoại bị đọc là **⛔ không hỏi giá** |
| **Filipino** | Nhóm **nhạy giá** và **`V3`** xa trung tâm | `V3` trông **dễ chốt hơn thật** |
| **Tiếng Hàn** | ★ Nhóm **`N1`** — khớp nhất với định vị K-beauty | Nhóm giá trị cao nhất ⛔ **không xuất hiện ở báo cáo nào** |
| **Farsi** | Khách của `Dr. Shilan` *(site công bố phục vụ Farsi)* | ⛔ Chưa rõ nhóm này lớn cỡ nào |

★ **Mọi báo cáo bắt buộc in dòng khai mẫu này.** ⛔ Không bỏ cho gọn — một mẫu lệch mà ⛔ không khai là một mẫu lệch người đọc **tưởng là đầy đủ**.

---

## Bốn lệnh

```bash
python tools/sw.py doc     du-lieu/hoi-thoai.md --ky "28/10-03/11"
python tools/sw.py insight --dong a          # hoặc --dong d
python tools/sw.py qc      --dong d
python tools/sw.py kiem    out/insight-d.json     # ★ CỔNG T
```

⛔ **Cố tình ⛔ không có lệnh `AUTO`.** Một file thì ⛔ không có tường nào; hai luồng có hai cổng và hai nhịp; và hai **dòng** có hai nhịp nội dung khác nhau nữa — nội dung thẩm mỹ chạy theo tuần, nội dung implant theo **tháng**.

### Chạy thử ngay khi chưa có dữ liệu thật

```bash
mkdir -p du-lieu && cp template/MAU_hoi-thoai.md du-lieu/
python tools/sw.py doc du-lieu/MAU_hoi-thoai.md --ky "28/10-02/11"
python tools/sw.py insight --dong d
python tools/sw.py qc      --dong d
```

---

## 14 sổ tri thức

| Sổ | Nội dung |
|---|---|
| [`sw-A`](knowledge/sw-A-vai-tro-hai-tuong.md) | **Vai trò · hai tường · bộ mã** · ba va chạm mã · CỔNG G · giá của việc chỉ đọc English |
| [`sw-B`](knowledge/sw-B-doc-dau-vao.md) | Đọc đầu vào · kênh PH · ẩn danh · `RA 10173` · ★ **ba bẫy khớp tiếng Anh** |
| [`sw-C`](knowledge/sw-C-hai-dong-hai-phe-u.md) | ★★ **Hai dòng · hai phễu · hai bộ rào** · `SD1`–`SD6` · `LÂU` · an toàn trước bán hàng |
| [`sw-D`](knowledge/sw-D-bang-du-kien-va-dau-ra.md) | Bảng dữ kiện gốc · cấu trúc file · ô `cheo` · sáu file đầu ra |
| [`sw-E`](knowledge/sw-E-module-sunwoo.md) | Module Sunwoo · ★ **ba chỗ hai site ⛔ không khớp** · 14 slot |
| [`sw-F`](knowledge/sw-F-hai-tuong-cong-t.md) | ★★ **Hai tường · CỔNG T tám câu** · bảng thẩm quyền · bốn cách tường bị phá |
| [`sw-G`](knowledge/sw-G-phap-ly-ph-cho-bao-cao.md) | Pháp lý PH cho báo cáo · ★ **câu ⛔ không dùng được** · chứng thực & ảnh |
| [`sw-I1`](knowledge/sw-I1-chan-dung-cong-0.md) | Chân dung · **CỔNG 0** · bốn nhãn · năm cổng ổn định |
| [`sw-I2`](knowledge/sw-I2-dao-sau-insight.md) | Câu hỏi ngầm · **ba nhánh rơi** · ★ **`% HOT*`** |
| [`sw-I3`](knowledge/sw-I3-ngan-hang-hook-en.md) | Hook English · ★ **8 hook viết được NGAY** · hook ⏸ bị chặn bởi slot nào |
| [`sw-I4`](knowledge/sw-I4-ma-tran-uu-tien.md) | Ma trận ưu tiên · **CỔNG 1** · ba nhịp |
| [`sw-Q1`](knowledge/sw-Q1-cham-diem-truc-page.md) | `TC-1`–`TC-10` · ★ **năm rào an toàn** · `TC-8` cộng điểm cho việc ⛔ không trả lời |
| [`sw-Q2`](knowledge/sw-Q2-co-do-phap-che.md) | `CĐ-S1`–`CĐ-S10` · ★ **miễn trừ xét trước** |
| [`sw-Q3`](knowledge/sw-Q3-so-tay-thuc-thi.md) | Sổ tay từng người · ★ mục *"⛔ không phải việc của bạn"* |

---

## ⚠️ Ba va chạm mã — đã biết, ⛔ không đổi tên

```
① "V"  ở đây = VÀNH ĐAI (V1–V4, PH)   ·  ở Paris = DỊCH VỤ (V-01…)
   → ở đây dịch vụ dùng DV-A* / DV-D*. ⛔ KHÔNG viết "V-01".
② "N"  ở đây = NHÓM KHÁCH (N1–N3)     ·  ở KNQT = TIÊU CHÍ (N1–N7)
   → ở đây tiêu chí dùng TC-*. ⛔ KHÔNG viết "N3.1".
③ "S"  = chặng dòng a  ·  "SD" = chặng dòng d
   → ⛔ KHÔNG viết "S4" khi nói về nha khoa. Viết "SD4".
```

---

## ⏸ Bảy slot 🔴 đang chặn

| Slot | Ai cấp | Chặn |
|---|---|---|
| ① ★ **Phạm vi giấy phép: một dòng hay hai** | Pháp chế | ⛔ **Chặn tất cả** |
| ② **Hotline đúng là số nào** — hai site lệch **4 số cuối** | Vận hành | Mọi hook có số gọi. ★ Gỡ bằng **một cuộc gọi thử** |
| ③ ★ **Khoảng tháng cắm → răng cuối** | Bác sĩ | **Toàn bộ rào `LÂU`** → chặng `SD4` |
| ④ **Số lần hẹn** một ca implant | Bác sĩ | Câu ③ của `LÂU` |
| ⑤ ★ **Có răng tạm trong lúc chờ không** | Bác sĩ | Câu ④ của `LÂU` — câu **gần như ⛔ không ai trả lời** |
| ⑥ **Tên hệ implant + số FDA PH** *(`DV-D1`)* | Vận hành + Pháp chế | Ô ⑦ checklist · `NGỜ`② |
| ⑦ ★ **Có nhận HMO nào không** | Vận hành | **Toàn bộ nhóm `N2`** dòng `d` — nhóm ngồi **ngay cạnh** phòng khám |

```
★ Hệ quả phải nói thẳng ở kỳ đầu:
  Repo ĐỌC được hội thoại nha khoa, ĐẾM được khách tắc ở đâu —
  nhưng ⛔ KHÔNG viết được một hook nào cho SD4.
  ⚠ Đó là trạng thái tệ nhất, vì nó TRÔNG như đang chạy.
```

Bảng đầy đủ **14 slot**: [`sw-E`](knowledge/sw-E-module-sunwoo.md) §5.

---

## ⛔ Dữ liệu

`du-lieu/` · `out/` · **`ma-nhan-vien.csv`** đã bị `.gitignore` chặn **từ commit đầu**. ⛔ Không commit, ⛔ không gửi qua kênh công khai.

★ **`out/doc-hoi-thoai.json` ⛔ không được gửi đi**, dù tên nó nghe như một file tạm — nó chứa nhánh `q`, tức là chứa `nv`.

---

## Tài liệu

| File | Nội dung |
|---|---|
| [`doc/01-cai-dat.md`](doc/01-cai-dat.md) | Ba cách cài · khuôn file hội thoại · **10 câu kiểm sau khi cài** |
| [`doc/CHANGELOG.md`](doc/CHANGELOG.md) | Quyết định kiến trúc · ★ **năm lỗi bắt được khi chạy thử** |
| [`prompts/`](prompts/) | 4 prompt: `đọc` · `insight` · `qc` · `tường ngăn` |
