# sw-I2 · ĐÀO SÂU INSIGHT · ĐỘ NÓNG

> Luồng **I**. Sổ này trả lời hai câu: **khách thật sự muốn hỏi gì**, và **họ rơi vì ai**.

---

## 1. CÂU HỎI NGẦM — THỨ KHÁCH ⛔ KHÔNG HỎI THẲNG

Khách hỏi một câu, nhưng câu đó thường là **phiên bản an toàn** của câu họ thật sự cần. Trả lời đúng câu được hỏi mà ⛔ không trả lời câu ngầm là cách mất khách mà ⛔ không ai biết vì sao.

| Khách gõ | Câu ngầm | Dòng |
|---|---|---|
| *"How much is thread lift?"* | *"Tôi có kham nổi việc này **lâu dài** không?"* | `a` · `BỀN` |
| *"Does it hurt?"* | *"Nếu có chuyện gì thì **ai xử lý cho tôi**?"* | cả hai · `SỢ` |
| *"Is it permanent?"* | *"Bao lâu nữa tôi lại phải tốn tiền?"* | `a` · `BỀN` |
| ★ *"Same day ba?"* | *"Tôi **phải thiếu răng bao lâu**?"* | `d` · `LÂU` |
| ★ *"Which implant do you use?"* | *"**Năm năm nữa** nó lung lay thì ai chịu?"* | `d` · `NGỜ` ② |
| *"Do you accept Maxicare?"* | *"Tôi **có phải tự trả** không?"* | `d` · `NGẠI` |
| *"Are you open Saturday?"* | *"Tôi **có phải xin nghỉ làm** không?"* | cả hai · `NGẠI` |
| *"Can I see actual cases?"* | *"Chỗ này **đã làm ca giống tôi** chưa?"* | cả hai · `NGỜ` |

> ★ **Hai dòng có đánh dấu ★ là hai câu ngầm quyết định của dòng `d`**, và ⛔ cả hai hiện ⛔ **không trả lời được** — slot ③④⑤ và slot ⑥⑧ ở `sw-E` §5.

⚠️ **Luật:** câu ngầm phải **suy từ lời khách trong chính hội thoại đó**, ⛔ không gán theo bảng này. Bảng này là **ví dụ về dạng**, ⛔ không phải bảng tra.

---

## 2. ★★ KHÁCH RƠI VÌ AI — BA NHÁNH, ⛔ ĐỪNG GỘP

> Đây là chỗ tách luồng trả tiền cao nhất. Cùng một hội thoại rơi, ba nhánh dẫn tới **ba việc khác nhau hoàn toàn** và **ba người khác nhau phải làm**.

| Nhánh | Dấu hiệu | Việc | Ai làm |
|---|---|---|---|
| ⛔ **HỆ** | Khách hỏi một thứ **hệ ⛔ chưa cấp số** để trả lời | Cấp dữ kiện | ★ **Phòng khám / bác sĩ / pháp chế** |
| **NỘI DUNG** | Khách hỏi một thứ **post đã hứa** mà trang đích ⛔ không có | Sửa post / thêm mục vào trang | **Marketing** |
| **NGƯỜI** | Hệ **đã cấp đủ**, post **⛔ không hứa sai**, mà nhân viên vẫn trả lời sai/né | Kèm cặp | Trưởng nhóm — ★ **qua luồng Q** |

### ★ Phép thử một câu, chạy **trước** khi gọi bất cứ gì là lỗi người

> *"Người giỏi nhất của khối, với đúng những gì hệ thống cấp hôm nay, có trả lời khác được không?"*

```
⛔ KHÔNG  →  nhánh HỆ. Vào mục "việc hệ thống", có tên người cấp.
             ⛔ KHÔNG vào luồng Q. ⛔ KHÔNG vào nội dung đào tạo.
✅ CÓ     →  có thể là nhánh NGƯỜI → chuyển luồng Q đối chiếu.
             ⚠ Nhưng luồng I ⛔ KHÔNG tự kết luận — nó ⛔ không có cột nv.
```

⚠️ **Ở dòng `d` kỳ đầu, nhánh HỆ gần như chắc chắn chiếm đa số**, vì **bảy slot 🔴** đang treo *(`sw-E` §5)*. Một báo cáo kỳ đầu mà nhánh NGƯỜI chiếm đa số là một báo cáo **chưa chạy phép thử trên**.

### Ví dụ — cùng một đoạn, ba cách đọc

```
KH: how long until I can eat normally after All-on-4?
NV: It depends on your case po. Can I get your number?
KH: ok thanks
<im>
```

| Nhánh | Đọc ra | ⛔ Có đúng không |
|---|---|---|
| **HỆ** | Hệ ⛔ **chưa cấp** khoảng tháng cho `DV-D4` *(slot ③)* → nhân viên ⛔ **không có gì để nói** | ★ **Đúng** — đây là nhánh thật |
| **NỘI DUNG** | Trang đích ⛔ không có mục *"timeline"* → khách phải hỏi | ★ **Cũng đúng** — hai nhánh **cùng lúc** |
| **NGƯỜI** | Nhân viên xin số thay vì trả lời | ⛔ **Chưa kết luận được** — xem phép thử. Và *"it depends"* **⛔ không sai**, nó chỉ **chưa đủ** |

★ **Hai nhánh đầu có thể cùng đúng**, và khi thế thì **cả hai phải được in**. ⛔ Không chọn một nhánh cho gọn — chọn một thì nhánh kia **⛔ không ai sửa**.

---

## 3. ĐỘ NÓNG — NĂM TÍN HIỆU

Mỗi hội thoại chấm năm tín hiệu, mỗi tín hiệu một bit:

| Bit | Tín hiệu | Dấu hiệu *(English)* |
|---|---|---|
| ① | **Nêu đúng một dịch vụ cụ thể** | gọi tên `DV-*`, ⛔ không hỏi chung *"what do you offer"* |
| ② | **Hỏi tiền** | `how much` · `total` · `price` · `package` · `installment` · `hmo` |
| ③ | **Hỏi thời gian / số buổi** | `how long` · `how many sessions` · `how many visits` · `same day` |
| ④ | **Nêu khu vực hoặc hỏi lịch** | `I'm in Makati` · `are you open Saturday` · `where exactly` |
| ⑤ | **Xin đặt lịch / tự cho liên hệ** | `can I book` · `what time tomorrow` · tự để lại số |

`do_nong` = số bit bật. ★ **4–5 bit = khách đang ở sát quyết định.**

### ★★ LUẬT CHỐNG VÒNG TRÒN — `% HOT*`

> ⚠️ **Đây là luật dễ bỏ qua nhất và nó làm sai mọi bảng xếp hạng nhóm.**

Năm tín hiệu ⛔ **không độc lập với cách chia nhóm**:

```
Chia nhóm theo DV-*        →  mọi hội thoại trong nhóm ĐÃ CÓ bit ① (định nghĩa)
Chia nhóm theo chặng S4/SD4 →  mọi hội thoại ĐÃ CÓ bit ② hoặc ③ (định nghĩa)
Chia nhóm theo rào BỀN/LÂU  →  ĐÃ CÓ bit ② hoặc ③
Chia nhóm theo vành đai     →  ĐÃ CÓ bit ④

★ Nên nhóm nào cũng "nóng hơn trung bình" — theo CẤU TRÚC, ⛔ không
  phải theo dữ liệu. Và kết luận "nhóm DV-D4 nóng nhất, dồn ngân sách
  vào đó" là một kết luận TỰ CHỨNG MINH CHÍNH NÓ.
```

★ **Bắt buộc:** mọi bảng so độ nóng giữa các nhóm phải có **thêm một cột `HOT*`** — tính lại **⛔ không có** tín hiệu đã bị cách chia nhóm cấy vào:

| Chia theo | `HOT*` bỏ bit |
|---|---|
| `DV-*` | ① |
| `chang` *(`S*` / `SD*`)* | ② ③ |
| `rao` | ② ③ |
| `vanh_dai` · `nhom` | ④ |
| `cd` *(chân dung)* | ★ **① ② ③** — chân dung dựng từ cả ba |

⛔ **Thiếu cột `HOT*` → bảng đó ⛔ không được dùng để xếp thứ tự ưu tiên.** Xem `sw-I4`.

---

## 4. HỘI THOẠI NGẮN — NHÓM ĐÔNG NHẤT, ⛔ HAY BỊ BỎ QUA NHẤT

```
Hội thoại ≤2 lượt khách  →  NHÓM RIÊNG, đọc TRƯỚC.
```

★ Nhóm này gần như luôn là nhóm đông nhất, và nó là nhóm **mất khách**: khách hỏi một câu, ⛔ không nhận được điều họ cần, rồi im. Hội thoại dài thì khách đã **ở lại** — tức là đã có gì đó đúng.

| Đọc gì từ nhóm ngắn | Ra việc gì |
|---|---|
| **Câu hỏi đầu tiên** của họ là gì | ★ Đó là câu phải trả lời **ngay trên trang đích**, ⛔ không để khách phải hỏi |
| Họ im **sau câu trả lời nào** | Câu trả lời đó đang ⛔ không gỡ được rào |
| Bao nhiêu % im sau khi bị **xin số** | ★ Nếu cao → thứ tự *"xin số trước / trả lời trước"* đang sai |

⚠️ **⛔ Không kết luận *"khách ⛔ không thật sự quan tâm"* từ hội thoại ngắn.** Đó là kết luận an toàn cho người viết báo cáo và ⛔ không dùng được cho ai. Một hội thoại hai lượt có **một câu hỏi thật** trong đó.

---

## 5. ★ `DV-A0` · `DV-D0` — DANH SÁCH DỊCH VỤ KHÁCH MUỐN MÀ ⛔ CHƯA CÓ

Hội thoại hỏi thứ ngoài danh sách công bố → `DV-A0` / `DV-D0`, và **ghi nguyên văn khách hỏi gì**.

★ Đây là một trong những đầu ra đáng tiền nhất của repo, vì nó là **nhu cầu có thật đang bị trả lời bằng "we don't offer that"**. Ví dụ dạng: chỉnh nha *(xem `sw-E` §2 ②)*, tẩy trắng, nhổ răng trẻ em, botox, nâng mũi.

⛔ **Nhưng ⛔ không biến nó thành đề xuất mở dịch vụ.** Repo này báo **nhu cầu**; quyết định mở dịch vụ phụ thuộc **phạm vi giấy phép** — và đó là ô 🔴 ① ở `sw-E` §5.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] Câu hỏi ngầm có **suy từ lời khách** chứ ⛔ không tra bảng §1?
- [ ] ★ **Phép thử một câu** đã chạy cho **từng** phát hiện trước khi gọi là lỗi người chưa?
- [ ] Có hội thoại nào bị gán nhánh **NGƯỜI** mà thật ra hệ ⛔ chưa cấp dữ kiện không?
- [ ] Hai nhánh **HỆ** và **NỘI DUNG** cùng đúng thì đã in **cả hai** chưa?
- [ ] ★ Mọi bảng so độ nóng đã có cột **`HOT*`** chưa?
- [ ] Nhóm hội thoại **≤2 lượt** đã đọc **trước** chưa?
- [ ] `DV-A0` / `DV-D0` đã ghi **nguyên văn** khách hỏi gì chưa?
- [ ] Luồng I có chỗ nào **tự kết luận về một người** không? *(⛔ không có cột `nv`)*
