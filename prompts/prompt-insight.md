# Prompt · `INSIGHT` — luồng I, **một dòng mỗi lần**

> ⛔ **Không có lệnh chạy cả hai dòng.** Hai dòng có hai phễu, hai bộ rào, hai nhịp nội dung — một lệnh gộp là một mẫu số trộn.

---

## ① Phác chân dung — dừng ở CỔNG 0

```
INSIGHT dòng <a|d>, kỳ <KỲ>.

① PHÁC CHÂN DUNG từ chính hội thoại của kỳ này.
   Mỗi chân dung mang ĐÚNG MỘT NHÃN:
     KHUÔN  — chân dung viết cho ads (CD1–CD6 của sổ nhập)
     PHÁC   — kỳ này, từ hội thoại thật  ⏸ chờ CỔNG 0
     CHUẨN  — đã duyệt sau ≥3 kỳ ổn định
     MỎNG   — n<10, ⛔ KHÔNG duyệt, in số tuyệt đối
   ⛔ Chân dung ⛔ không nhãn → người đọc mặc định nó là CHUẨN.

② MỖI CHÂN DUNG CẦN BA THỨ:
   · ≥3 TRÍCH NGUYÊN VĂN lời khách, mỗi trích có HT-nnn
     ⛔ "Khách quan tâm giải pháp phục hồi răng" là MỘT CÂU RỖNG —
       một người chưa đọc hội thoại nào cũng viết được câu đó.
   · CÂU HỎI NGẦM — câu khách thật sự muốn hỏi mà ⛔ không hỏi thẳng
   · VIỆC NỘI DUNG — và nếu nó bị SLOT chặn thì ghi rõ SLOT NÀO

③ NĂM CỔNG ỔN ĐỊNH, chạy cho DÒNG NÀY RIÊNG:
   ① phủ ≥80%  ② ⛔ không chân dung nào >45%  ③ bền qua kỳ
   ★④ KHÁC VIỆC — hai chân dung phải dẫn tới HAI việc khác nhau
   ⑤ mỗi chân dung có MỘT rào nặng nhất rõ ràng
   ★ Cổng ④ hay bị bỏ qua nhất: hai chân dung CÙNG MỘT VIỆC thì
     chúng là MỘT chân dung bị chia hai vì nhân khẩu học.

④ ĐỐI CHIẾU với CD1–CD6 của sổ nhập: khớp / ⛔ không khớp ở chỗ nào.
   ★ Chỗ ⛔ KHÔNG KHỚP là phát hiện đáng đọc nhất của bước này.

⑤ ⏸ DỪNG Ở CỔNG 0. ⛔ KHÔNG tự duyệt. ⛔ KHÔNG viết hook.
   ★ NHƯNG: mục VIỆC HỆ THỐNG và CỜ ĐỎ ĐẾM TỔNG đi được NGAY —
     đó là dữ kiện về HỆ THỐNG CỦA CHÚNG TA, ⛔ không phải kết luận
     về khách.
```

---

## ② Đào sâu — ba nhánh rơi

```
Khách rơi vì ai? BA NHÁNH, ⛔ ĐỪNG GỘP:

⛔ HỆ      — khách hỏi thứ hệ ⛔ CHƯA CẤP SỐ  → cấp dữ kiện  → phòng khám
NỘI DUNG  — khách hỏi thứ post ĐÃ HỨA mà trang ⛔ không có → sửa post → Marketing
NGƯỜI     — hệ đã cấp, post ⛔ không hứa sai, mà vẫn trả lời sai → kèm cặp → luồng Q

★ PHÉP THỬ, chạy TRƯỚC khi gọi bất cứ gì là lỗi người:
  "Người giỏi nhất của khối, với đúng những gì hệ thống cấp hôm nay,
   có trả lời khác được không?"
  ⛔ KHÔNG → nhánh HỆ. ⛔ KHÔNG vào luồng Q, ⛔ không vào đào tạo.

⚠ HAI NHÁNH ĐẦU CÓ THỂ CÙNG ĐÚNG → in CẢ HAI.
  Chọn một nhánh cho gọn thì nhánh kia ⛔ KHÔNG AI SỬA.

⚠ Kỳ đầu dòng d: nhánh HỆ gần như chắc chắn chiếm đa số (7 slot 🔴).
  Một báo cáo kỳ đầu mà nhánh NGƯỜI chiếm đa số là báo cáo CHƯA
  chạy phép thử trên.
```

---

## ③ Độ nóng — ★ bắt buộc có cột `HOT*`

```
Năm tín hiệu: ① nêu một dịch vụ cụ thể ② hỏi tiền ③ hỏi thời gian/số buổi
              ④ nêu khu vực hoặc hỏi lịch ⑤ xin đặt lịch / tự cho liên hệ

★★ CHỐNG VÒNG TRÒN — tín hiệu ⛔ KHÔNG độc lập với cách chia nhóm:
   chia theo DV-*   → ĐÃ CÓ bit ① theo định nghĩa
   chia theo chặng  → ĐÃ CÓ bit ②③
   chia theo rào    → ĐÃ CÓ bit ②③
   chia theo vành đai → ĐÃ CÓ bit ④
   chia theo chân dung → ĐÃ CÓ ①②③

→ Nhóm nào cũng "nóng hơn trung bình" THEO CẤU TRÚC. Và kết luận
  "dồn ngân sách vào nhóm nóng nhất" là kết luận TỰ CHỨNG MINH CHÍNH NÓ.

★ Bảng ⛔ KHÔNG có cột HOT* → ⛔ KHÔNG được dùng xếp ưu tiên.
★ Cột đáng tin là HOT*; cái đáng chú ý là KHOẢNG CHÊNH.
  Chênh lớn = độ nóng phần lớn do CÁCH CHIA NHÓM, ⛔ không do khách.
⚠ ⛔ Không so HOT* CHÉO cách chia nhóm (chân dung bỏ 3 bit nên luôn thấp).
```

---

## ④ Hai thứ hay bị bỏ

```
★ HỘI THOẠI ≤2 LƯỢT KHÁCH → NHÓM RIÊNG, ĐỌC TRƯỚC.
  Nhóm này gần như luôn đông nhất và nó là nhóm MẤT KHÁCH.
  Hội thoại dài thì khách ĐÃ Ở LẠI — tức là đã có gì đó đúng.
  Đọc: câu hỏi ĐẦU TIÊN của họ · họ im sau câu trả lời nào ·
       bao nhiêu % im sau khi bị XIN SỐ
  ⛔ KHÔNG kết luận "khách ⛔ không thật sự quan tâm" — đó là kết luận
    an toàn cho người viết báo cáo và ⛔ không dùng được cho ai.

★ DV-A0 / DV-D0 — dịch vụ khách MUỐN mà cơ sở ⛔ CHƯA CÔNG BỐ.
  Ghi NGUYÊN VĂN khách hỏi gì. Đây là nhu cầu có thật đang bị trả lời
  bằng "we don't offer that".
  ⛔ Nhưng ⛔ không biến nó thành đề xuất mở dịch vụ — việc đó phụ thuộc
    PHẠM VI GIẤY PHÉP, là ô 🔴 ① còn treo.
```

---

## ⑤ Ô `cheo` — mẫu số là **TỔNG KỲ**

```
⚠ Chỗ dễ sai nhất của cả repo:

6 hội thoại hỏi cả hai dòng · kỳ có 73 HT (a=52 · d=21)

✅ 6/73 = 8%    ← mẫu số TỔNG KỲ
⛔ 6/52 = 12%   ← "12% khách thẩm mỹ hỏi sang nha khoa"
⛔ 6/21 = 29%   ← "29% khách nha khoa hỏi sang thẩm mỹ"

★ Cùng SÁU hội thoại, BA con số. Cả ba trông hợp lý. Và 52+21=73
  nên tổng VẪN KHỚP — ⛔ không ai phát hiện.
```

---

```bash
python tools/sw.py insight --dong a
python tools/sw.py insight --dong d
python tools/sw.py kiem out/insight-d.json     # ★ CỔNG T trước khi gửi
```
