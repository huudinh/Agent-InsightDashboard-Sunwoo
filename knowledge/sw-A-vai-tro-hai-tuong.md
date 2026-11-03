# sw-A · VAI TRÒ · HAI TƯỜNG · BỘ MÃ

> Sổ đọc đầu tiên. Nó trả lời ba câu: **agent này làm gì**, **cái gì ⛔ không đi qua được tường nào**, và **mã nào đã có rồi nên ⛔ không được đặt lại**.

---

## 1. AGENT NÀY LÀM GÌ

Đọc **hội thoại khách nhắn vào** của **Sunwoo Medical Center** — một cơ sở ở Ground floor, 20 Upper McKinley Hill, Taguig, Metro Manila — rồi trả hai thứ cho hai người khác nhau:

```
LUỒNG I · INSIGHT KHÁCH  → Marketing
   khách là ai · họ ở chặng nào · họ đang vướng rào nào ·
   kỳ tới viết gì · hook nào đáng thử

LUỒNG Q · QC TRỰC PAGE   → trưởng nhóm trực page
   ai đang trượt tiêu chí nào · bằng chứng là cặp câu nào ·
   việc nào là lỗi hệ chứ ⛔ không phải lỗi người
```

### ★ Và cơ sở này có HAI DÒNG DỊCH VỤ

| Dòng | Site | Là gì |
|---|---|---|
| **`a`** · thẩm mỹ | <https://sunwooaesthetic.ph/> | Da liễu – thẩm mỹ nội khoa, **không phẫu thuật**, phần lớn **nhiều buổi** |
| **`d`** · nha khoa | <https://sunwoodental.ph/> | **Implant** · veneer · nhổ răng khôn · nha khoa tổng quát |

⚠️ **Hai dòng này ⛔ không phải hai phòng khám.** Cùng địa chỉ, cùng đầu số, site nha khoa tự gọi mình là *"Sunwoo Medical Center"*. Nhưng **quyết định mua của hai dòng khác nhau về bản chất** — xem `sw-C` §1 — nên mọi tỷ lệ phải tách.

---

## 2. ⛔ NHỮNG VIỆC AGENT NÀY ⛔ KHÔNG LÀM

| Việc | Của ai |
|---|---|
| Nghiên cứu từ khoá · sinh mẫu quảng cáo · dựng landing · chẩn đoán chỉ số ads | ★ `Agent-AdsOptimize-Phi` |
| Duyệt pháp chế câu chữ ở PH | **Pháp chế phòng khám** — agent chỉ **rà và đánh dấu** |
| Duyệt chuyên môn y khoa / nha khoa | **Bác sĩ** |
| Quyết định nhân sự · kỷ luật · xếp hạng công khai | ⛔ **Không ai trong agent này** |
| Trả lời khách · sửa CRM | ⛔ **Không agent nào** |

### ★★ LUẬT SỔ NHẬP TỪ NGOÀI

Repo `Agent-AdsOptimize-Phi` **đã có** bốn sổ về chính thương hiệu này và chính thị trường này. Agent này **nhập** chúng, ⛔ **không viết lại**:

| Sổ nhập | Chứa gì | Khi mâu thuẫn |
|---|---|---|
| `kn-ho-so-thuong-hieu-sunwoo.md` | Định danh · 6 dịch vụ thẩm mỹ · 2 bác sĩ · con số site công bố · **6 lỗi trang production** | ★ **Sổ đó thắng** |
| `kn-vung-philippines.md` | **Bốn vành đai `V1`–`V4`** · ba nhóm `N1`–`N3` · ngôn ngữ · kênh · tiền tệ · mùa vụ | ★ **Sổ đó thắng** |
| `kn-rao-phap-ly-ph.md` | Hai tầng rào · **checklist 12 ô** · lời chứng thực & ảnh trước/sau · **Data Privacy Act RA 10173** · bảng từ cấm | ★ **Sổ đó thắng** |
| `kn-chan-dung-hanh-trinh-ph.md` | **Phễu `S1`–`S6`** · **bốn rào `SỢ·NGỜ·NGẠI·BỀN`** · **sáu chân dung `CD1`–`CD6`** | ★ **Sổ đó thắng** |

⚠️ **Bốn sổ đó viết cho dòng `a` thẩm mỹ.** Phần nào của chúng ⛔ không áp được cho dòng `d` nha khoa thì `sw-C` nói rõ, và chỉ phần đó mới được viết mới.

> ⛔ **Không nạp tri thức của `Agent-InsightDashboard-Kangnam` · `-Paris` · `-KNQT` vào cùng project.** Cả ba dùng bộ mã khác, luật hiển thị giá khác, và **luật pháp lý của một nước khác** *(Việt Nam `91/2025/QH15`)*. Ở đây là **Philippines `RA 10173`** — hai luật khác nhau về nghĩa vụ, và trộn vào thì agent sẽ trích luật sai nước.

---

## 3. ★★ HAI TƯỜNG — HAI LOẠI KHÁC NHAU

Đây là chỗ repo này khác mọi bản InsightDashboard trước: nó có **hai tường**, và chúng ⛔ **không cùng loại**. Hiểu sai chỗ này là dựng ra một repo phức tạp gấp bốn mà ⛔ không chặn được gì.

```
TƯỜNG D · theo DÒNG          TƯỜNG L · theo LUỒNG
chặn việc TRỘN SỐ            chặn việc LỌT TÊN

"tỷ lệ chốt 38%"             "chị Kay trượt TC-4"
 ⛔ của a hay của d?           ⛔ đi vào file Marketing đọc

Vi phạm = một con số          Vi phạm = một con người
trông hợp lý mà ⛔ không       bị nêu tên trong một file
nói về ai cả                  ⛔ không dành cho người đó
```

| | **TƯỜNG D** *(dòng)* | **TƯỜNG L** *(luồng)* |
|---|---|---|
| Chặn gì | ⛔ Không **tỷ lệ** nào có mẫu số trộn `a` + `d` | ⛔ Không **file** nào có cả tên nhân viên và lời khách |
| Đơn vị bị chặn | **Phép chia** | **Trường dữ liệu** |
| Kiểm bằng | Mỗi tỷ lệ phải mang nhãn dòng | Tìm khoá bị chặn + tìm tên trong chuỗi |
| Đi qua được không | ✅ **Có** — xem §4 | 🔶 **Một chiều** — chỉ cờ đỏ, đã lọc tên (`sw-F` §6) |

### ★ Vì sao hai tường này **cộng** vào nhau chứ ⛔ không **nhân** lên

Tường L chặn **chỗ đặt dữ liệu**: tên nhân viên nằm ở nhánh `q`, ⛔ không bao giờ ở nhánh `i`. Tường D chặn **phép tính**: một tỷ lệ chỉ được lấy mẫu số trong cùng một dòng.

Hai thứ đó tác động lên **hai tầng khác nhau**, nên cấu trúc chỉ cần lồng **một lần**:

```
out/doc-hoi-thoai.json
{
  "ky": "…",
  "a": { "i": [ … ], "q": [ … ] },     ← tường L nằm ở đây
  "d": { "i": [ … ], "q": [ … ] }
    ↑
  tường D nằm ở đây
}
```

⚠️ **⛔ Không dựng bốn file rời `a-i`, `a-q`, `d-i`, `d-q` ở bước đọc.** Bốn file rời thì bốn lần đọc, và bốn lần đọc thì **bốn bộ số lệch nhau** — mà số lệch nhau là thứ phá hỏng mọi báo cáo nhanh hơn bất cứ lỗi nào khác. Đọc **một lần**, lồng nhánh, rồi xuất ra file theo nhánh.

---

## 4. ★ TƯỜNG D ĐI QUA ĐƯỢC — NHƯNG CHỈ BA THỨ

Tường D ⛔ không phải tường kín. Khách của hai dòng là **cùng một tập người ở cùng một khu**, nên có ba thứ **phải** đọc chung, nếu không thì mất đúng cái lợi thế của việc có hai dòng trong một cơ sở:

| Đi qua được | Vì sao | ⛔ Nhưng |
|---|---|---|
| **Vành đai `V1`–`V4`** | Cùng một quãng đường tới McKinley Hill. Khách ở Makati mất 30 phút dù đi trị nám hay đi cắm implant | ⛔ Không gộp **tỷ lệ chốt** theo vành đai cho cả hai dòng |
| **Nhóm `N1`–`N3`** | Cộng đồng Hàn ở McKinley Hill · expat BGC · OFW — ba nhóm này cắt ngang cả hai dòng | ⛔ Không kết luận *"nhóm `N1` khó chốt"* từ số trộn |
| ★ **Khách dùng cả hai dòng** | Đây là **tài sản riêng** của cơ sở này: một khách làm veneer rồi hỏi trị nám. ⛔ Đối thủ chỉ có một dòng thì ⛔ không có dữ kiện này | Đếm ở **mục riêng** `cheo`, ⛔ không nhập vào phễu của dòng nào |

### ★★ Ô `cheo` — thứ đáng giá nhất mà ⛔ dễ bị đánh mất nhất

> Một khách nhắn *"how much for veneers?"* rồi ba tin sau hỏi *"do you also do melasma?"* là **một dữ kiện ⛔ không dòng nào tự nhìn thấy được**. Ở báo cáo của dòng `d` nó là một ca veneer. Ở báo cáo của dòng `a` nó ⛔ **không tồn tại**.

Vì vậy bảng dữ kiện gốc có cột `dong_hoi` là **danh sách**, ⛔ không phải một giá trị. Hội thoại hỏi cả hai dòng thì `dong_hoi = ["a","d"]`, và nó:

- vào phễu của **cả hai** dòng *(vì khách thật sự hỏi cả hai)*
- vào ô `cheo` **một lần**
- ⛔ **không** được đếm hai lần trong tổng số hội thoại của kỳ

⚠️ **Luật mẫu số của ô `cheo`:** tỷ lệ chéo lấy mẫu số là **tổng hội thoại của kỳ**, ⛔ không phải tổng của một dòng. Lấy mẫu số một dòng thì cùng một con số sẽ ra **hai tỷ lệ khác nhau** tuỳ chọn dòng nào — và cả hai đều trông hợp lý.

---

## 5. BỐN CỔNG CHẶN

| Cổng | Chặn gì | Ai mở | Máy chạy? |
|---|---|---|---|
| **CỔNG 0** | ⛔ Chưa duyệt chân dung → ⛔ không viết hook, ⛔ không ra việc | Người | ⬜ |
| ★ **CỔNG G** | ⛔ Chưa cắt được theo vành đai → ⛔ không kết luận | Máy chặn, người xác nhận | ✅ |
| **CỔNG 2** | ⛔ Chưa qua rà pháp lý PH → ⛔ không xuất bản chạy được | Pháp chế | 🔶 rà tự động, duyệt bằng người |
| ★★ **CỔNG T** | ⛔ Trượt tường → **từ chối ghi file** | ⛔ Không ai mở được | ✅ **`sys.exit(2)`** |

### ★ CỔNG G — cổng riêng của bản Philippines

`kn-vung-philippines.md` §1 đặt **CỔNG GEO** cho phía ads: mọi dòng từ khoá phải `geo_mode = Presence`. Ở phía đọc hội thoại, cùng một ràng buộc có **một dạng khác**:

```
Hội thoại ⛔ không có dấu hiệu khu vực  →  V0 (chưa biết)

V0 ≥ 20% mẫu của kỳ  →  ⛔ DỪNG, hỏi người, ⛔ KHÔNG kết luận theo vành đai.
```

**Vì sao đây là cổng chứ ⛔ không phải một ô cảnh báo:** phòng khám có **một cơ sở**, khách phải **đến tận nơi**. Một báo cáo nói *"nhóm trị nám chốt kém"* mà ⛔ không biết nhóm đó ở đâu là một báo cáo ⛔ không dùng được — vì rất có thể họ chốt kém **chỉ vì họ ở Quezon City và ⛔ không ai vượt EDSA 70 phút để trị nám một buổi**. Đó ⛔ không phải vấn đề tư vấn, đó là vấn đề vành đai, và hai việc đó cần hai cách sửa khác nhau.

⚠️ Trường `Your area` trên form **đang là ô text tự do** *(`kn-ho-so-thuong-hieu-sunwoo.md` §7)* → khi đọc hội thoại, phần lớn vành đai phải **suy từ lời khách**, và suy thì sai được. Vì vậy `V0` là một giá trị **thật**, ⛔ không phải một ô rỗng cần điền cho đủ.

---

## 6. ★★ BỘ MÃ — CÁI GÌ ĐÃ CÓ, CÁI GÌ MỚI

> ⛔ **LUẬT CỨNG: ⛔ không bao giờ đặt một mã mới cho một thứ đã có mã.** Đặt trùng nghĩa khác là cách chắc chắn nhất để hai sổ cùng nói về một thứ mà ⛔ không ai nhận ra.

### Mã NHẬP — ⛔ không sửa, ⛔ không đổi tên, ⛔ không mở rộng nghĩa

| Mã | Nghĩa | Nguồn | Dùng cho dòng |
|---|---|---|---|
| `V1` `V2` `V3` `V4` | **Bốn vành đai** theo phút đi lại tới McKinley Hill | `kn-vung-philippines.md` §2 | ★ **cả hai** |
| `N1` `N2` `N3` | Hàn Quốc McKinley Hill · expat BGC · OFW | `kn-vung-philippines.md` §3 | ★ **cả hai** |
| `S1`…`S6` | Phễu 6 chặng, chặng quyết định `S4` | `kn-chan-dung-hanh-trinh-ph.md` §3 | **`a`** |
| `SỢ` `NGỜ` `NGẠI` `BỀN` | Bốn rào cản | `kn-chan-dung-hanh-trinh-ph.md` §2 | **`a`** |
| `CD1`…`CD6` | Sáu chân dung gốc | `kn-chan-dung-hanh-trinh-ph.md` §4 | **`a`** |

★ **Một giá trị mở rộng, ⛔ không phải một bộ mã mới:** `V0` = **chưa biết vành đai**. Nó là giá trị thứ năm của bộ `V` đã có, cần vì đọc hội thoại ⛔ không có trường `Your area` như form. Xem §5.

### Mã MỚI — chỉ đặt cho thứ ⛔ chưa có mã nào

| Mã | Nghĩa | Vì sao phải mới |
|---|---|---|
| `DV-A1`…`DV-A6` | Sáu dịch vụ dòng thẩm mỹ | Sổ nhập liệt kê tên dịch vụ nhưng ⛔ không đánh mã |
| `DV-D1`…`DV-D7` | Bảy dịch vụ dòng nha khoa | ⛔ Chưa có sổ nào nói về dòng này |
| `SD1`…`SD6` | **Phễu dòng nha khoa** | ⚠ Xem `sw-C` §3 — ⛔ không tái dùng `S1`–`S6` |
| `LÂU` | **Rào thứ tư của dòng nha khoa** | `BỀN` là *"bao lâu lại phải làm tiếp"*; `LÂU` là *"bao lâu mới xong"* — hai câu khác nhau |
| `CD-D1`…`CD-D6` | Chân dung dòng nha khoa | `CD1`–`CD6` là chân dung thẩm mỹ, ⛔ không gán lại |
| `TC-1`…`TC-10` | **Mười ô chấm trực page** | ⛔ Không dùng chữ `N` — `N1`–`N3` đã là **nhóm khách** ở sổ nhập |
| `CĐ-S1`…`CĐ-S10` | Cờ đỏ pháp chế PH | Dựng từ `kn-rao-phap-ly-ph.md` §2 và §7 |

### ⚠️ BA VA CHẠM ĐÃ BIẾT — ⛔ không đổi tên, ghi kèm ngữ cảnh

```
① "V" ở repo này   = VÀNH ĐAI (V1–V4, PH)
   "V" ở Paris     = DỊCH VỤ  (V-01…V-11, nha khoa VN)
   → Ở đây dịch vụ dùng DV-A* / DV-D*. ⛔ KHÔNG viết "V-01".

② "N" ở repo này   = NHÓM KHÁCH (N1–N3, PH)
   "N" ở KNQT      = TIÊU CHÍ CHẤM (N1–N7)
   → Ở đây tiêu chí dùng TC-*. ⛔ KHÔNG viết "N3.1".

③ "S" ở repo này   = CHẶNG PHỄU THẨM MỸ (S1–S6)
   "SD" ở repo này = CHẶNG PHỄU NHA KHOA (SD1–SD6)
   → ⛔ KHÔNG viết "S4" khi nói về nha khoa. Viết "SD4".
```

★ **Quy ước viết:** luôn ghi kèm dòng khi mã có thể nhầm — *"chặng `S4` dòng thẩm mỹ"*, *"rào `LÂU` dòng nha khoa"*. ⛔ Không viết mã trần ở chỗ hai dòng đứng cạnh nhau.

---

## 7. NGÔN NGỮ ĐẦU VÀO — ENGLISH, VÀ ⚠️ ĐIỀU ĐÓ CÓ GIÁ

Bản này đọc hội thoại **tiếng Anh**. Khớp từ khoá dựng theo **ranh giới từ** tiếng Anh, ⛔ không dùng bộ khớp tiếng Việt.

⚠️ **Nhưng `kn-vung-philippines.md` §4 nói rõ bốn thứ tiếng có thật trong hội thoại ở PH**, và bỏ ba thứ còn lại ⛔ không phải là trung tính — nó **lệch mẫu theo đúng những nhóm đáng chú ý nhất**:

| ⏸ Chưa đọc được | Mất nhóm nào | Hệ quả thật |
|---|---|---|
| **Taglish** *(trộn Anh–Tagalog trong một câu)* | Nhóm nhắn qua **Messenger**, kênh số 1 ở PH | *"magkano po ang thread lift"* ⛔ không khớp `price` → hội thoại đó bị đọc là **⛔ không hỏi giá** |
| **Filipino / Tagalog thuần** | ★ Nhóm **nhạy giá** và nhóm **`V3` xa trung tâm** | Vành đai xa nhất bị **đọc thiếu**, nên `V3` trông dễ chốt hơn thật |
| **Tiếng Hàn** | ★ Nhóm **`N1`** — nhóm khớp nhất với định vị K-beauty | Nhóm có giá trị cao nhất ⛔ **không xuất hiện trong báo cáo nào** |
| **Farsi** | Khách của `Dr. Shilan Hassanalizadeh` *(site nha khoa công bố phục vụ Farsi)* | ⛔ Chưa biết nhóm này lớn cỡ nào |

> ★ **Luật bắt buộc khi xuất báo cáo:** mọi báo cáo phải in dòng
> *"Mẫu kỳ này **chỉ gồm hội thoại tiếng Anh**. ⛔ Chưa đọc được: Taglish · Filipino · Hàn · Farsi. Vì vậy ⛔ không kết luận về nhóm `N1` và ⚠ số của `V3` có thể đang **đọc thiếu**."*

⛔ **Không bỏ dòng này cho gọn.** Một mẫu lệch mà ⛔ không khai là một mẫu lệch mà người đọc tưởng là đầy đủ — và đó là cách một con số đúng về mặt tính toán dẫn tới một quyết định sai.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Có mã nào mới được đặt cho một thứ **đã có mã** ở bốn sổ nhập không?
- [ ] Có tỷ lệ nào mẫu số trộn `a` + `d` không? *(tường D)*
- [ ] Có file nhánh `i` nào chứa tên nhân viên không? *(tường L — kiểm **bằng máy**)*
- [ ] `V0` của kỳ này bao nhiêu phần trăm? ≥20% thì **đã dừng** chưa? *(CỔNG G)*
- [ ] Hội thoại hỏi cả hai dòng đã vào ô `cheo` **một lần** và ⛔ không bị đếm hai lần trong tổng kỳ chưa?
- [ ] Báo cáo đã in dòng khai **mẫu chỉ có tiếng Anh** chưa?
- [ ] Khi mâu thuẫn với sổ nhập, đã lấy **sổ nhập** chưa?
