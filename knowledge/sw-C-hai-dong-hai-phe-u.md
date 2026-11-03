# sw-C · ★★ HAI DÒNG · HAI PHỄU · HAI BỘ RÀO

> Sổ lõi nhất của repo. Nó trả lời: **vì sao ⛔ không gộp hai dòng vào một phễu được**, và **mỗi dòng mất khách ở đâu**.

---

## 1. ★★ HAI DÒNG KHÁC NHAU Ở QUYẾT ĐỊNH MUA, ⛔ KHÔNG Ở DỊCH VỤ

Nếu khác nhau chỉ ở *"một bên làm da, một bên làm răng"* thì một cột `dong` là đủ. Nhưng khác nhau thật nằm ở **hình dạng của quyết định**:

| | **`a` · THẨM MỸ** | **`d` · NHA KHOA** |
|---|---|---|
| Hình tiền | **Nhiều lần nhỏ**, lặp lại | ★ **Một lần lớn**, ⛔ không lặp |
| Hình thời gian | Mỗi buổi 30–90 phút, cách nhau vài tuần | ★ **Nhiều tháng** — chờ xương liền |
| Kết quả | **Có thời hạn**, hết thì làm lại | **Vĩnh viễn hoặc gần vĩnh viễn** |
| Câu hỏi khoá | *"Năm sau tôi còn phải trả bao nhiêu?"* | *"Bao lâu thì tôi có răng?"* |
| Rào thứ tư | **`BỀN`** | ★ **`LÂU`** |
| Khách đổi ý vì | Tính ra tổng 12 tháng thì ⛔ không kham nổi | Nghe *"chờ 4 tháng"* thì bỏ |
| Nếu ⛔ không làm | Trông già hơn — **chịu được** | ⚠️ **Tiêu xương, lệch khớp** — ⛔ không chịu được mãi |

### ★ Dòng cuối là dòng quan trọng nhất của bảng này

Khách thẩm mỹ **có thể không làm gì cả** và cuộc sống vẫn tiếp tục. Khách mất răng thì **không**: để lâu là tiêu xương, và tiêu xương làm chính ca implant sau này **đắt hơn và lâu hơn**.

> ⚠️ Nhưng điều đó ⛔ **không** cho phép dùng làm đòn ép bán. Nói *"để lâu là mất xương"* trong quảng cáo ở PH rơi vào ô ⑥ của checklist 12 ô — **chẩn đoán trong quảng cáo** — và ô ⑤ nếu kèm chê ngoại hình. Xem `sw-G`.
>
> ★ Cách đúng: trả lời **khi khách hỏi**, bằng cơ chế và bằng mốc thời gian, ⛔ không bằng tính từ gây lo. *"Bone loss starts within months of tooth loss, which is why we take a CBCT first"* là thông tin. *"Don't wait or you'll lose your jaw"* là ép.

### ⛔ Hệ quả: một con số trộn hai dòng ⛔ không nói về ai

```
"Tỷ lệ khách hỏi giá rồi im = 44%"

Dòng a: khách tính ra 6 buổi × ₱X rồi thấy quá sức
         → sửa bằng BẢNG LIỆU TRÌNH + tổng gói   (nội dung)
Dòng d: khách nghe tổng ₱XXX,XXX cho All-on-4
         → sửa bằng TRẢ GÓP / HMO                 (chính sách)

Một con số 44%, HAI việc phải làm khác nhau hoàn toàn.
★ Và người đọc sẽ chọn MỘT việc — thường là việc của dòng đông hơn.
```

---

## 2. DÒNG `a` · THẨM MỸ — ⛔ KHÔNG VIẾT MỚI, DÙNG SỔ NHẬP

Dòng này **đã có đủ tri thức** ở `Agent-AdsOptimize-Phi`. Agent ⛔ **không viết lại**:

| Thứ | Lấy ở | Mã |
|---|---|---|
| Phễu 6 chặng, chặng quyết định `S4` | `kn-chan-dung-hanh-trinh-ph.md` §3 | `S1`…`S6` |
| Bốn rào, rào thứ tư `BỀN` + **bốn câu của `BỀN`** | cùng sổ §2 | `SỢ` `NGỜ` `NGẠI` `BỀN` |
| Sáu chân dung gốc | cùng sổ §4 | `CD1`…`CD6` |
| Sáu dịch vụ | `kn-ho-so-thuong-hieu-sunwoo.md` §2 | ★ xem dưới |

### Sáu dịch vụ dòng `a` — đặt mã để cắt báo cáo

| Mã | Dịch vụ *(đúng tên trên form)* | Nhóm | Giá trị ca |
|---|---|---|---|
| `DV-A1` | **Meso Hair Therapy** | Tóc | Cao *(nhiều buổi)* |
| `DV-A2` | **Skin Rejuvenation** *(Filler · HA Collagen Booster)* | Da — trẻ hoá | Trung bình–Cao |
| `DV-A3` | **Xline Thread Lift** | Nâng cơ | ★ **Cao nhất dòng `a`** |
| `DV-A4` | **Acne Treatment** | Da — bệnh lý | Thấp–Trung bình |
| `DV-A5` | **Melasma Treatment** *(PicoSure Pro)* | Da — sắc tố | Trung bình–Cao *(liệu trình)* |
| `DV-A6` | **Scar Treatment** | Da — bệnh lý | Thấp–Trung bình |

⛔ **Ngoài sáu mã này → `DV-A0` ngoài phạm vi**, và ghi nguyên văn khách hỏi gì. ⚠️ `DV-A0` ⛔ không phải rác: nó là **danh sách dịch vụ khách muốn mà cơ sở ⛔ chưa công bố**, và đó là một trong những đầu ra đáng tiền nhất của cả repo.

---

## 3. ★★ DÒNG `d` · NHA KHOA — PHẦN DUY NHẤT PHẢI VIẾT MỚI

⛔ **Không có sổ nào trong hệ sinh thái nói về dòng này.** Và ⛔ không tái dùng phễu `S1`–`S6`: chặng quyết định khác, thứ tự rào khác.

### Bảy dịch vụ dòng `d`

| Mã | Dịch vụ *(đúng tên trên site)* | Nhóm | Giá trị ca |
|---|---|---|---|
| `DV-D1` | **Smart Bio Implant** | Implant | ⚠️ xem cảnh báo dưới |
| `DV-D2` | **Single Implant** | Implant | Cao |
| `DV-D3` | **Implant Bridge** | Implant | Rất cao |
| `DV-D4` | **All-on-4 & All-on-6** | Implant toàn hàm | ★ **Cao nhất cả cơ sở** |
| `DV-D5` | **Porcelain & Veneers** | Thẩm mỹ răng | Cao |
| `DV-D6` | **Wisdom Extraction** | Tiểu phẫu | Thấp |
| `DV-D7` | **General Dentistry** | Tổng quát | ★ Thấp — **nhưng xem §4** |

> ⚠️ **`DV-D1` "Smart Bio Implant" là một tên thương mại, ⛔ không phải một loại implant có tên chuẩn.** Ô ⑦ của checklist 12 ô yêu cầu **tên thiết bị phải khớp đăng ký FDA PH**. `[CHỜ XÁC NHẬN]` đây là hệ implant nào, hãng nào, số đăng ký FDA PH bao nhiêu. ⛔ Chưa có → agent ⛔ không viết hook nào dùng tên này.

### PHỄU `SD1`–`SD6` — chặng quyết định là **`SD4`**

| Chặng | Dấu hiệu trong lời khách *(English)* | Rào |
|---|---|---|
| **`SD1` NHẬN BIẾT** | `missing tooth` · `what is a dental implant` · `can i still get implant` | — |
| **`SD2` SO SÁNH CÁCH LÀM** | `implant vs bridge` · `vs dentures` · `all-on-4 or all-on-6` · `veneers or crown` | `NGỜ` ① |
| **`SD3` NỖI SỢ & AN TOÀN** | `does it hurt` · `is extraction painful` · `sedation` · `implant failure` · `am i too old` | **`SỢ`** |
| ★★ **`SD4` THỜI GIAN & SỐ LẦN HẸN** | `how long does it take` · `how many visits` · `how long until i get the tooth` · `bone graft` · `healing` · `same day` | ★ **`LÂU`** |
| **`SD5` TIỀN & CÁCH TRẢ** | `how much` · `total cost` · `installment` · `hmo` · `maxicare` · `card` | `NGẠI` |
| **`SD6` CHỌN NƠI & BẢO HÀNH** | `which implant brand` · `who will do it` · `warranty` · `book` · `aftercare` | `NGỜ` ② |

### ★ Vì sao `SD4` là chặng của dòng này

Khách đến `SD4` **đã vượt `SỢ` và đã chấp nhận là sẽ tốn tiền**. Họ chỉ đang tính một thứ: **bao lâu thì xong**.

- Cả ngành implant quảng cáo *"same-day teeth"*. Khách ⛔ **không biết** rằng phần lớn ca phải chờ **xương liền 3–6 tháng** giữa hai giai đoạn, và họ chỉ phát hiện ra **khi đã ngồi trên ghế**.
- Site của chính cơ sở này đang bán đúng vào rào đó: *"2× faster bone integration"*. ⚠️ Đó là **một claim về thời gian**, và nó là bằng chứng rằng rào `LÂU` là rào thật của dòng này.
- Mất khách ở `SD4` là mất đắt nhất: họ đã tin bác sĩ, đã chấp nhận giá, rồi nghe *"bốn tháng"* và biến mất ⛔ không nói gì.

> **Phép thử trước khi xuất bất kỳ hook nào của dòng `d`:**
> *"Đọc xong, khách có biết **từ hôm nay đến lúc có răng ăn được** là bao lâu và bao nhiêu lần hẹn không?"*
> Chưa → chưa xong.

**Bốn câu của rào `LÂU`, theo đúng thứ tự khách nghĩ:**

| # | Khách nghĩ | Phải trả lời bằng |
|---|---|---|
| 1 | *"Hôm nay đi, hôm nay có răng không?"* | **Có / không, và vì sao** — ⛔ không trả lời bằng *"tuỳ trường hợp"* rồi hết |
| 2 | *"Tổng cộng bao lâu?"* | **Một khoảng tháng** + mốc nào xảy ra lúc nào |
| 3 | *"Phải đến mấy lần?"* | **Một con số lần hẹn** |
| 4 | *"Trong lúc chờ tôi ăn uống thế nào, có răng tạm không?"* | ★ Câu **gần như ⛔ không ai trả lời** — và là câu quyết định với khách còn đi làm |

⛔ Chưa có bốn con số này *(`[CHỜ XÁC NHẬN]` — bác sĩ cấp)* thì agent ⛔ **không viết hook `SD4`**, và ô tương ứng ở luồng Q chấm `—`, ⛔ **không trừ điểm nhân viên**.

### ★ `NGỜ` của dòng `d` xuất hiện HAI LẦN — và lần thứ hai mới là lần mất ca

| | `NGỜ` ① ở `SD2` | ★ `NGỜ` ② ở `SD6` |
|---|---|---|
| Khách hỏi | *"Chỗ này có nha sĩ thật không?"* | *"Dùng implant hãng nào? Ai cắm? Bảo hành ra sao nếu 5 năm nữa nó lung lay?"* |
| Gỡ bằng | PRC license · D.M.D./D.D.M. · phòng khám có thật | ★ **Tên hệ implant + số đăng ký FDA PH · tên người cắm · T&C bảo hành bằng văn bản** |
| Nếu ⛔ không gỡ | Khách ⛔ không nhắn tiếp | ⚠️ **Khách đã chấp nhận giá rồi mới rơi** — mất ca đắt nhất |

★ Đây là khác biệt thật so với dòng `a`: ở thẩm mỹ, `NGỜ` là rào **đầu phễu**; ở nha khoa, `NGỜ` còn là rào **cuối phễu**, vì khách đang mua một thiết bị phải sống trong miệng họ **hai mươi năm**.

⚠️ Site đang công bố *"written warranty on veneers and crowns"* và *"100% FDA-approved implants"*. **Cả hai câu đều ⛔ không dùng được nguyên văn** — `100%` nằm trong bảng từ cấm, và *"written warranty"* đã bị ghi là **lỗi ③** ở `kn-ho-so-thuong-hieu-sunwoo.md` §6. Xem `sw-G` §2.

### Sáu chân dung dòng `d` — khuôn kỳ đầu

> ⚠️ **Sáu chân dung này là GIẢ THUYẾT KỲ ĐẦU**, ⛔ không phải bộ chân dung đã duyệt. Chúng dựng từ nội dung site + bảy dịch vụ + bối cảnh PH, ⛔ **chưa có một hội thoại thật nào**. CỔNG 0 ở `sw-I1` tồn tại chính vì điều này.

| Mã | Ai | Lời khách *(dạng thật, English)* | Rào nặng nhất | Vào ở |
|---|---|---|---|---|
| `CD-D1` | Nam/nữ 45–65, mất 1–2 răng hàm, đi làm | *"I lost a molar two years ago. Is it too late to get an implant?"* | **`LÂU`** + `NGẠI` | `SD1`–`SD4` |
| `CD-D2` | 55+, mất gần hết răng, đang dùng tháo lắp | *"My dentures keep slipping. How many visits for All-on-4?"* | ★ **`LÂU`** | `SD2`–`SD4` |
| `CD-D3` | Nữ 22–35, veneer vì thẩm mỹ | *"How many teeth do you need to shave for veneers?"* | **`SỢ`** *(mài răng thật)* | `SD2`–`SD3` |
| `CD-D4` | 18–30, răng khôn đau | *"My wisdom tooth hurts, can I walk in today?"* | `SỢ` | `SD3` → ⚠️ xem §5 |
| `CD-D5` | ★ Đã cắm ở nơi khác, ⛔ không ổn | *"I had an implant elsewhere and it's loose now."* | **`NGỜ` ②** nặng nhất | `SD3`–`SD6` |
| `CD-D6` | Nhân sự công ty có **HMO** | *"Is your clinic HMO-accredited? I have Maxicare."* | `NGẠI` | `SD5` |

★ **`CD-D6` là chân dung chỉ có ở Philippines.** HMO *(Maxicare · Medicard · Intellicare…)* là cách rất nhiều nhân sự văn phòng BGC/Makati tiếp cận nha khoa, và **câu đầu tiên của họ ⛔ không phải giá, mà là *"có nhận HMO không"***.

> `[CHỜ XÁC NHẬN]` **cơ sở có nhận HMO nào không, và cho dịch vụ nào.**
> ⛔ Thiếu ô này thì toàn bộ nhóm `N2` *(expat & nhân sự văn phòng BGC)* ở dòng `d` ⛔ **không trả lời được** — và `N2` chính là nhóm ngồi ngay cạnh phòng khám.

⚠️ `CD-D5` *(đã cắm ở nơi khác)* là chân dung **trả được chi phí cao nhất** và cũng là chân dung **dễ chấm sai nhất** — xem §6.

---

## 4. ★ CÁI GÌ ĐỌC CHUNG — VÀ MỘT Ô CHỈ CƠ SỞ NÀY CÓ

Ba thứ đi qua tường D *(`sw-A` §4)*: **vành đai `V1`–`V4`** · **nhóm `N1`–`N3`** · **ô `cheo`**.

### `DV-D7 General Dentistry` là cửa vào, ⛔ không phải dịch vụ rẻ

Nhìn theo giá trị ca thì `DV-D7` là dịch vụ thấp nhất của cả cơ sở. Nhưng nó là dịch vụ:

- khách **tự tìm đến** mà ⛔ không cần quảng cáo gỡ rào nào,
- khách **quay lại định kỳ**, nên là chỗ duy nhất cơ sở **gặp khách khi họ chưa có nhu cầu gì**,
- và là chỗ khách **ngồi trên ghế đủ lâu** để một câu *"chị có muốn xem luôn về nám không"* trở thành tự nhiên thay vì thành bán chéo thô.

★ Vì vậy ô `cheo` phải cắt được theo **dịch vụ cửa vào**: hội thoại nào vào bằng `DV-D7` rồi hỏi sang dòng `a`, và ngược lại dòng `a` nào hỏi sang `DV-D5` veneer.

⛔ **Nhưng ⛔ không biến phát hiện này thành chỉ tiêu bán chéo cho nhân viên trực page.** Luồng Q chấm **chất lượng tư vấn**, ⛔ không chấm số lượt gợi dịch vụ thứ hai — ép thế thì mọi hội thoại đều kết thúc bằng một câu chào hàng, và đó là cách nhanh nhất làm hỏng chính ô `cheo`.

### ⚠️ Nhóm `N1` Hàn Quốc — cắt ngang hai dòng, và **⛔ chưa đọc được**

`kn-vung-philippines.md` §3 ghi `N1` là nhóm khớp nhất với định vị K-beauty và nói **tiếng Hàn**, kênh **KakaoTalk**. Bản này đọc **tiếng Anh** → `N1` gần như ⛔ **không xuất hiện trong mẫu**.

★ Và với dòng `d` thì điều đó còn nặng hơn: một cộng đồng Hàn ở ngay McKinley Hill, có nhu cầu nha khoa như mọi cộng đồng khác, **ngay cạnh một phòng implant**. ⛔ Repo này hiện ⛔ không nói được gì về nhóm đó. Ghi thẳng điều đó trong báo cáo, ⛔ **không im lặng** — xem `sw-A` §7.

---

## 5. ★★ AN TOÀN TRƯỚC BÁN HÀNG — HAI DÒNG, HAI DANH SÁCH

> Hội thoại có **dấu hiệu cấp tính** thì nó ⛔ **không còn là một cơ hội bán**. Nó là một ca cần bác sĩ **hôm nay**.

```
Có dấu hiệu cấp tính  →  ① chuyển bác sĩ / hẹn khám ngay
                          ② ⛔ KHÔNG nêu giá
                          ③ ⛔ KHÔNG gợi dịch vụ thứ hai
                          ④ ⛔ KHÔNG chấm các ô TC về xin số, về chốt hẹn bán
```

### Dòng `a` · dấu hiệu cấp tính

| Dấu hiệu | Vì sao gấp |
|---|---|
| ★ **Đau nhiều · da trắng bệch · mờ mắt · đau mắt sau tiêm filler** | 🔴 Nghi **tắc mạch do filler** — là **cấp cứu**, có cửa sổ thời gian tính bằng giờ |
| Sưng tăng · nóng đỏ · chảy dịch · sốt sau thủ thuật | Nghi nhiễm trùng |
| Nốt cứng · loét · hoại tử da vùng tiêm | Biến chứng mạch máu / nhiễm trùng sâu |
| Phát ban toàn thân · khó thở · sưng môi-mắt sau tiêm | Nghi phản vệ |

### Dòng `d` · dấu hiệu cấp tính

| Dấu hiệu | Vì sao gấp |
|---|---|
| ★ **Sưng mặt lan · sốt · khó mở miệng · khó thở hoặc khó nuốt** | 🔴 Nghi **nhiễm trùng răng lan vào vùng cổ mặt** — đường thở, là cấp cứu |
| Chảy máu ⛔ không cầm sau nhổ răng | Cấp cứu chảy máu |
| Đau dữ dội 3–5 ngày sau nhổ | Nghi viêm ổ răng khô |
| Implant lung lay · mủ quanh implant · tê môi kéo dài | Nghi thất bại implant / tổn thương thần kinh |

### ⚠️ HAI BẪY CỦA PHẦN NÀY — cả hai đã xảy ra thật ở repo khác

```
BẪY ①  Đưa từ của CHỈ ĐỊNH LÀM LẠI vào danh sách cấp tính.
        "loose", "failed", "my old implant" ⛔ KHÔNG phải cấp tính —
        đó là CD-D5, chân dung đắt nhất của dòng d.
        → Gán cấp tính cho nó = miễn hết các ô chấm
        = ⛔ MẤT PHẦN KHEN ĐÚNG cho một ca tư vấn tốt.
        ★ "loose NOW + mủ + tê"  ≠  "loose, I want it redone"

BẪY ②  Gán cấp tính theo TỪ KHOÁ ĐƠN LẺ.
        "pain" một mình ⛔ không phải cấp tính — "does it hurt?"
        là câu hỏi của chặng SD3, là hội thoại BÁN HÀNG bình thường.
        ★ Phải có: dấu hiệu + DẤU HIỆU ĐANG XẢY RA (now, since, still,
          getting worse, days after) mới thành cấp tính.
```

★ Vì vậy máy phân **hai bậc**, ⛔ không một bậc:

| Bậc | Nghĩa | Hệ quả |
|---|---|---|
| `cap-tinh` | Dấu hiệu **+ đang diễn tiến** | ⛔ Không bán · miễn các ô `TC` về bán |
| `can-bs` | Có dấu hiệu nhưng ⛔ chưa rõ đang diễn tiến | 🔶 Vẫn chuyển bác sĩ, **nhưng vẫn chấm bình thường** |
| `""` | ⛔ Không dấu hiệu | Hội thoại bán hàng bình thường |

⛔ **Chỉ bậc `cap-tinh` mới kích hoạt luồng ⛔ không bán.**

---

## 6. ★ "LÀM Ở ĐÂU" LÀ DỮ KIỆN ĐỘC LẬP

Khách kể mình **đã làm rồi** thì phải biết **làm ở đâu** — và đó là **một trường riêng**, ⛔ **không khoá sau mã dịch vụ nào**:

| `lam_o_dau` | Nghĩa | Hội thoại này là gì |
|---|---|---|
| `tai-sunwoo` | Đã làm **tại cơ sở này** | ⚠️ **Khách đang phản ánh / cần hậu mãi** — ⛔ không phải cơ hội bán mới |
| `noi-khac` | Đã làm **ở nơi khác**, ⛔ không hài lòng | ★ `CD5` / `CD-D5` — **trả được chi phí cao nhất** |
| `""` | ⛔ Chưa làm ở đâu | Khách mới |

> ⚠️ **Lỗi đã xảy ra thật ở hai repo trước:** gán `lam_o_dau` **chỉ khi** mã dịch vụ đã rơi vào một nhóm nhất định. Kết quả: một hội thoại phản ánh *(khách đã làm tại cơ sở, đang không hài lòng)* được mã sang nhóm khác nên ⛔ **không bao giờ nhận được nhãn phản ánh** — và nó được chấm như **một cơ hội bán**.
>
> ★ **Luật:** nhận `lam_o_dau` bằng **logic độc lập** *(có tên cơ sở / có dấu hiệu "đã làm" như `had`, `got it done`, `last year`, `two months ago`)*, chạy **trước** và **không phụ thuộc** mọi mã khác.

★ Với dòng `d`, `tai-sunwoo` còn nặng hơn: một implant đã cắm tại cơ sở mà **lung lay** là **trách nhiệm bảo hành**, và site đang công bố *"written warranty"*. Hội thoại đó phải được gắn nhãn `phan-anh` và vào **mục riêng**, ⛔ không nằm lẫn trong phễu bán.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Có tỷ lệ nào lấy mẫu số trộn `a` + `d` không?
- [ ] Hook dòng `d` nào trả lời được **cả bốn** câu của rào `LÂU` chưa? Chưa thì đã ghi `[CHỜ XÁC NHẬN]` chưa?
- [ ] Có dùng tên `Smart Bio Implant` trong hook nào không? *(⛔ chưa có số đăng ký FDA PH)*
- [ ] Ô HMO đã hỏi chưa? Chưa thì nhóm `N2` dòng `d` đã được ghi là ⛔ **không trả lời được** chưa?
- [ ] Hội thoại `CD-D5` *(implant cũ lung lay)* có bị gán `cap-tinh` oan không? → kiểm **bậc hai** §5
- [ ] `lam_o_dau` có được nhận **độc lập** với mọi mã dịch vụ không?
- [ ] Hội thoại `tai-sunwoo` đã ra **mục phản ánh riêng** chưa, hay còn nằm trong phễu bán?
- [ ] Sáu chân dung `CD-D*` vẫn đang mang nhãn **giả thuyết kỳ đầu** chứ?
