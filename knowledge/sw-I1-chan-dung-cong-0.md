# sw-I1 · CHÂN DUNG & CỔNG 0

> Luồng **I**. Sổ này trả lời: **khách là ai**, và **khi nào được phép nói mình đã biết họ là ai**.

---

## 1. ★★ HỆ NÀY ⛔ KHÔNG CÓ BỘ CHÂN DUNG ĐÃ DUYỆT — CẢ HAI DÒNG

Đây là trạng thái thật, ⛔ không phải một ô còn trống chờ điền:

| Dòng | Có gì | Trạng thái |
|---|---|---|
| **`a`** | `CD1`–`CD6` ở `kn-chan-dung-hanh-trinh-ph.md` §4 | ⚠️ **KHUÔN cho ads**, dựng từ nội dung site + bối cảnh PH — ⛔ **không dựng từ hội thoại thật** |
| **`d`** | `CD-D1`–`CD-D6` ở `sw-C` §3 | ⚠️ **GIẢ THUYẾT KỲ ĐẦU** — ⛔ **chưa có một hội thoại thật nào** |

★ **Vì vậy chế độ mặc định là: PHÁC HỌA THEO KỲ.** Mỗi kỳ agent **phác lại chân dung từ chính hội thoại của kỳ đó**, rồi **dừng ở CỔNG 0** chờ người duyệt.

⛔ **Đây là chế độ TẠM, ⛔ không phải cách làm đúng lâu dài.** Ba điều kiện để nghỉ chế độ tạm:

```
① Dòng đó đã có ≥3 kỳ liên tiếp, mỗi kỳ ≥50 hội thoại.
② Bộ chân dung phác ra ở ba kỳ đó ỔN ĐỊNH — xem §3.
③ Người có thẩm quyền đã duyệt bộ đó thành BỘ CHUẨN, bằng văn bản.

⛔ Thiếu một điều kiện → vẫn phác lại mỗi kỳ. ⛔ KHÔNG tự nghỉ cổng.
```

> ⚠️ **Vì sao ⛔ không dùng thẳng `CD1`–`CD6` của sổ nhập:** sáu chân dung đó dựng để **chọn từ khoá và viết landing**, tức là dựng từ **giả thuyết về người gõ tìm kiếm**. Repo này đọc **người đã nhắn tin** — một tập khác, hẹp hơn và đã vượt qua một bước lọc. Dùng thẳng thì agent sẽ **đi tìm bằng chứng cho sáu chân dung có sẵn** thay vì đọc xem thật ra ai đang nhắn.
>
> ★ Nhưng ⛔ **không bỏ chúng đi**: dùng làm **bộ đối chiếu**. Mỗi kỳ in thêm một dòng *"chân dung phác ra khớp / ⛔ không khớp `CD-x` của sổ nhập ở chỗ nào"* — và chỗ ⛔ **không khớp** chính là phát hiện đáng đọc nhất.

---

## 2. ★ BỐN NHÃN — ⛔ ĐỪNG TRỘN

Bốn thứ dưới đây hay bị gọi chung là *"chân dung"*, và trộn chúng là cách làm một báo cáo ⛔ không ai dùng được:

| Nhãn | Là gì | Dựng từ | Ai duyệt |
|---|---|---|---|
| `KHUÔN` | Chân dung viết cho ads | Nội dung site + bối cảnh | ⛔ Không ai — đã có sẵn |
| ★ `PHÁC` | Chân dung **kỳ này**, từ hội thoại thật | ≥50 HT của **một dòng** | ⏸ **Chờ CỔNG 0** |
| `CHUẨN` | Bộ đã duyệt thành chính thức | ≥3 kỳ ổn định | ✅ Người có thẩm quyền |
| `MỎNG` | Nhóm **⛔ chưa đủ mẫu** để gọi là chân dung | <10 HT | ⛔ Không duyệt — **in số tuyệt đối** |

⛔ **Mọi chân dung trong mọi đầu ra phải mang đúng một nhãn.** Một chân dung ⛔ không nhãn thì người đọc mặc định nó là `CHUẨN` — và họ sẽ đem nó đi dựng kế hoạch nội dung cả quý.

---

## 3. ★ NĂM CỔNG ỔN ĐỊNH — PHÉP THỬ "BỘ NÀY DÙNG ĐƯỢC CHƯA"

Chạy cho **từng dòng riêng**, ⛔ không gộp:

| # | Cổng | Trượt thì nghĩa là |
|---|---|---|
| ① | **Phủ** — ≥80% hội thoại của dòng xếp được vào một chân dung | Bộ **quá hẹp**; phần ⛔ không xếp được là chân dung còn thiếu |
| ② | **Tách** — ⛔ không chân dung nào chiếm >45% | Bộ **quá thô**; chân dung lớn nhất đang gộp hai nhóm |
| ③ | **Bền** — một `HT` đọc lại kỳ sau vẫn xếp vào **cùng** chân dung | Tiêu chí xếp đang mơ hồ |
| ④ | ★ **Khác việc** — hai chân dung bất kỳ phải dẫn tới **hai việc nội dung khác nhau** | Hai chân dung **cùng một việc** → chúng là **một** chân dung |
| ⑤ | **Khớp rào** — mỗi chân dung có **một** rào nặng nhất rõ ràng | Chưa đọc được khách vướng gì |

> ★ **Cổng ④ là cổng quan trọng nhất và hay bị bỏ qua nhất.** Hai chân dung khác nhau về tuổi, về khu vực, về giọng kể — mà **cùng cần một trang trả lời một câu** — thì chúng là **một** chân dung bị chia hai vì lý do nhân khẩu học. Chia như thế làm bộ chân dung trông chi tiết hơn mà ⛔ không làm được việc gì hơn.

---

## 4. CỔNG 0 — AGENT DỪNG Ở ĐÂU

```
B1 ĐỌC         → bảng gốc, V0, CỔNG G
B2 PHÁC        → chân dung nhãn PHÁC, cho TỪNG dòng riêng
B3 ĐỐI CHIẾU   → khớp/⛔ không khớp KHUÔN của sổ nhập ở chỗ nào
B4 ⏸ CỔNG 0   → DỪNG. In bộ PHÁC + năm cổng ổn định + câu hỏi cần duyệt
─────────────── ⛔ KHÔNG tự đi qua ───────────────
B5 ĐÀO SÂU     → sw-I2
B6 HOOK        → sw-I3
B7 MA TRẬN     → sw-I4
```

⛔ **Agent ⛔ không tự duyệt CỔNG 0.** Và ⛔ không viết hook cho một chân dung nhãn `PHÁC` chưa duyệt — vì hook là thứ đi ra ngoài, và một hook viết cho một chân dung sai là **một tuần nội dung mất**.

★ **Nhưng CỔNG 0 ⛔ không chặn mọi thứ:** phần **việc hệ thống** *(`sw-F` §7)* và phần **cờ đỏ đếm tổng** **đi được ngay**, ⛔ không cần duyệt. Chúng là dữ kiện về **hệ thống của chúng ta**, ⛔ không phải kết luận về khách.

---

## 5. KHUÔN MỘT CHÂN DUNG `PHÁC`

```
CD-D2 · [PHÁC · kỳ 28/10–03/11 · dòng d · n=7 → ⚠ MỎNG]

AI        : 55+, mất gần hết răng hàm dưới, đang dùng tháo lắp
VÀO Ở     : SD2 (so sánh All-on-4 với tháo lắp)
RÀO NẶNG  : LÂU
VÀNH ĐAI  : V2 ×4 · V3 ×2 · V0 ×1
BẰNG CHỨNG: ★ ba trích nguyên văn, lời khách, đã ẩn danh
  · "my dentures keep slipping when I eat"            (HT-023)
  · "how many visits will it take, I live in Makati"  (HT-031)
  · "can I have teeth while waiting for the healing"  (HT-044)
CÂU HỎI NGẦM: "tôi còn phải sống không răng bao lâu nữa"
VIỆC NỘI DUNG: ⏸ chờ slot ③④⑤ (sw-E §5) — ⛔ chưa viết được hook SD4
⚠ MỎNG: n=7 <10 → in SỐ TUYỆT ĐỐI, ⛔ KHÔNG in phần trăm
```

**Ba thứ bắt buộc, thiếu một là chân dung ⛔ không dùng được:**

1. ★ **Bằng chứng là lời khách nguyên văn**, ≥3 trích, mỗi trích có `HT-nnn`. *"Khách quan tâm giải pháp phục hồi răng"* là **một câu rỗng** — nó ⛔ không nói gì mà một người ⛔ chưa đọc hội thoại nào cũng viết được.
2. **Câu hỏi ngầm** — câu khách thật sự muốn hỏi nhưng ⛔ không hỏi thẳng. Xem `sw-I2`.
3. ★ **Việc nội dung** — chân dung ⛔ không dẫn tới một việc thì nó là một đoạn văn, ⛔ không phải một chân dung. Và nếu việc đó **đang bị chặn bởi một slot** thì ghi rõ **slot nào**.

---

## 6. ⚠️ BA CÁCH PHÁC SAI — ĐỀU IM LẶNG

```
① PHÁC THEO NHÂN KHẨU HỌC
   "Nữ 28–35, Makati, thu nhập trung bình cao" — đó là một ô target
   quảng cáo, ⛔ KHÔNG phải một chân dung. Nó ⛔ không nói khách SỢ gì.
   ★ Phép thử: đọc xong có biết viết câu đầu của trang đích không?

② PHÁC THEO DỊCH VỤ
   "Nhóm khách veneer" — đó là tên một DV-*, ⛔ không phải chân dung.
   ★ CD-D3 (sợ mài răng thật) và một khách veneer đã quyết rồi chỉ
     hỏi giá là HAI chân dung, dù cùng DV-D5.

③ ★ PHÁC TỪ HỘI THOẠI DÀI NHẤT
   Hội thoại dài nhất là hội thoại dễ đọc nhất, nên nó chiếm chỗ.
   ⚠ Nhưng hội thoại NGẮN NHẤT mới là chỗ mất khách: khách hỏi một
     câu, ⛔ không được trả lời điều họ cần, rồi im.
   ★ Luật: đếm hội thoại ≤2 lượt khách thành MỘT NHÓM RIÊNG và đọc
     nó trước. Đó là nhóm đông nhất và ⛔ gần như luôn bị bỏ qua.
```

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Mọi chân dung đã mang **đúng một nhãn** *(`KHUÔN`/`PHÁC`/`CHUẨN`/`MỎNG`)* chưa?
- [ ] Phác **riêng từng dòng** chứ ⛔ không gộp `a` + `d`?
- [ ] Năm cổng ổn định đã chạy cho **từng dòng** chưa? Đặc biệt **cổng ④**?
- [ ] Mỗi chân dung có **≥3 trích nguyên văn** kèm `HT-nnn` chưa?
- [ ] Có chân dung nào ⛔ **không dẫn tới một việc** không?
- [ ] Có hook nào đã viết cho chân dung nhãn `PHÁC` **chưa duyệt** không?
- [ ] Nhóm hội thoại **≤2 lượt khách** đã được đọc **riêng** chưa?
- [ ] Dòng đối chiếu *"khớp / ⛔ không khớp `KHUÔN`"* đã in chưa?
