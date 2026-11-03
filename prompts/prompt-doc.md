# Prompt · `ĐỌC` — một lần đọc, hai dòng, hai nhánh

> Bước này ⛔ **không kết luận gì**. Nó trả lời: **cái gì trong kỳ này đọc được, và cái gì ⛔ không**.

---

```
ĐỌC hội thoại kỳ <KỲ>.

Đính kèm: <file hội thoại>  ·  <số ads cùng kỳ, nếu có>

── IN TRƯỚC MỌI CON SỐ ──
① TỔNG HT PHÂN BIỆT  —  ⚠ ⛔ KHÔNG bằng n(a) + n(d)
   (hội thoại hỏi cả hai dòng nằm trong CẢ HAI nhánh)
② n(a) · n(d) · n(chéo) · ⏸ n(chưa rõ dòng)
   ★ ⛔ KHÔNG đoán dòng. ⛔ Không có dấu hiệu dòng nào → ⛔ KHÔNG vào
     phễu của dòng nào — vào sai dòng là vào sai MẪU SỐ.
③ ★ CỔNG G: V0 là bao nhiêu phần trăm?
   V0 ≥ 20% → ⛔ DỪNG. ⛔ KHÔNG kết luận theo vành đai. Hỏi tôi.
④ ⏸ CỘT THIẾU: thiếu giờ → TC-1 "—" · thiếu kênh → ⛔ không đọc giờ trực
   · thiếu NV → ⛔ không vào nhánh q
⑤ ★ HỆ QUẢ: liệt kê CHÍNH XÁC cái gì đọc được và cái gì ⏸

⛔ Chưa in ô ③ và ⑤ thì ⛔ KHÔNG chạy tiếp.

── BẮT BUỘC, mọi lần ──
"Mẫu kỳ này chỉ gồm hội thoại tiếng Anh. ⛔ Chưa đọc được: Taglish ·
 Filipino · Hàn · Farsi. Vì vậy ⛔ không kết luận về nhóm N1, và số
 của V3 có thể đang đọc thiếu."
```

---

## ★ ẨN DANH NGAY Ở BƯỚC NÀY, ⛔ không ở bước xuất

```
tên khách        → KH-001
số điện thoại    → ⛔ BỎ HẲN (⛔ không băm, ⛔ không giữ 4 số cuối)
email · link     → ⛔ BỎ HẲN
địa chỉ cụ thể   → vành đai V1–V4   ★ vành đai là thứ cần, số nhà thì ⛔ không
ảnh khách gửi    → [ảnh: vùng điều trị]  ⛔ KHÔNG lưu ảnh
tên nhân viên    → NV-xx  (bảng quy đổi do trưởng nhóm giữ, ⛔ ngoài out/)
```

⚠️ **Đổi ở bước xuất thì tên thật còn lại trong mọi file trung gian** — và một trong số đó **sẽ** bị gửi đi. Đổi ở bước đọc thì ⛔ **không có bản nào chứa tên để mà lọt**.

### Dữ liệu sức khoẻ · `RA 10173`

```
Tiền sử · bệnh nền · thuốc · ảnh · phim  →  NHÃN + MỘT CÂU BẰNG CHỨNG.
⛔ KHÔNG chép nguyên văn đoạn khách kể bệnh sử.

★ Nhân viên PHẢI HỎI (dòng d: đái tháo đường · chống đông ·
  bisphosphonate — ảnh hưởng chỉ định implant).
  Báo cáo CHỈ LƯU NHÃN. Hai việc khác nhau.
```

---

## ⚠️ BỐN THỨ DỄ ĐỌC SAI

```
① [Thẻ: …]  ⛔ KHÔNG phải một lượt khách.
   Đếm nó là lượt khách → câu hỏi đầu tiên bị đọc sai, mốc TC-1 sai, và
   tỷ lệ "hội thoại ⛔ không có câu hỏi nào" vọt lên → báo cáo kết luận
   "mẫu bị lọc", một kết luận ⛔ KHÔNG có thật.

② "your clinic" trong câu HỎI ⛔ KHÔNG phải "tôi đã làm ở đây".
   "Is your clinic HMO-accredited?" là khách MỚI.
   ★ `tai-sunwoo` cần CẢ dấu hiệu "đã làm" (had · got · months ago…).

③ `tai-sunwoo` MỘT MÌNH ⛔ KHÔNG phải phản ánh.
   tai-sunwoo + DẤU HIỆU VẤN ĐỀ  → phan-anh  (hậu mãi, mục riêng)
   tai-sunwoo + ⛔ không vấn đề   → quay-lai  ★ TÀI SẢN, đọc cùng ô `cheo`
   ⚠ Gán sai chiều này biến một ca bán thêm thành một ca khiếu nại.

④ "loose, I want it redone" ⛔ KHÔNG phải cấp tính.
   Đó là CD-D5 — chân dung ĐẮT NHẤT dòng d.
   ★ Cấp tính = DẤU HIỆU + ĐANG DIỄN TIẾN (now · since · still ·
     getting worse · days after). Một từ đơn lẻ thì CHƯA ĐỦ.
```

---

## Google Sheet / dán tay

★ Đọc **trong chat** qua connector — `sw.py` ⛔ không có quyền truy cập Sheet. Dán link + nói rõ tab nào là gì.

Đoạn **dán tay** ⛔ không có khuôn `HT-nnn` → gắn nhãn `nguồn dán tay`, ghi nguyên văn vào phụ lục, và ⛔ **không vào ngưỡng mẫu** của bất kỳ kết luận nào.

---

```bash
python tools/sw.py doc du-lieu/hoi-thoai.md --ky "28/10-03/11"
```
