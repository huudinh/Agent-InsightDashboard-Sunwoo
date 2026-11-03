# sw-Q2 · CỜ ĐỎ PHÁP CHẾ — `CĐ-S1`…`CĐ-S10`

> Luồng **Q**. Cờ đỏ ⛔ **không phải lỗi tư vấn** — nó là **rủi ro pháp lý ở Philippines**.
> ★ Mỗi mã nối về **đúng một ô** của checklist 12 ô *(`kn-rao-phap-ly-ph.md` §2)*, ⛔ không phải một bảng mới.

---

## 1. ★★ LUẬT ĐỌC TRƯỚC MỌI THỨ: XÉT MIỄN TRỪ **TRƯỚC**

> ⚠️ **Lỗi nặng nhất mà hệ này có thể mắc ⛔ không phải bỏ sót một cờ. Đó là nêu cờ cho một người đang làm ĐÚNG.**

```
NV: "I can't promise a specific result — only the doctor can assess
     that after your consultation. We don't guarantee outcomes."
                 ↑                                      ↑
            chứa "promise"                       chứa "guarantee"

Khớp từ khoá đơn thuần  →  nêu CĐ-S1 "cam kết kết quả"
★ Trong khi đây là người ĐANG TỪ CHỐI cam kết, đúng quy trình.
```

★ **Luật:** mỗi mã có **danh sách cụm miễn trừ**, máy xét **trước**. Khớp miễn trừ → ⛔ **không nêu cờ**, và nếu ô `TC` tương ứng đang xét thì **chấm `✓`**.

| Cụm miễn trừ *(English)* | Miễn cho |
|---|---|
| `can't promise` · `cannot guarantee` · `we don't guarantee` · `no one can guarantee` · `results vary` · `depends on your condition` | `CĐ-S1` |
| `only the doctor can` · `the doctor will assess` · `after your consultation` · `we'd need to examine` | `CĐ-S1` `CĐ-S3` |
| `let me confirm` · `I'll check with the clinic` · `I'll get back to you` · `I don't want to give you a wrong number` | ★ `CĐ-S5` |
| `we don't offer that` · `that's outside what we do` · `we'd have to refer you` | `CĐ-S4` |
| `I'd need the patient's consent first` · `we only share cases with written consent` | ★ `CĐ-S6` |
| `I'll have to check our FDA registration` | `CĐ-S8` |

> ★ **Hai dòng đánh dấu ★ là hai dòng đáng khen nhất và dễ bị phạt oan nhất.**
> ① *"let me confirm with the clinic"* khi hệ **chưa cấp** số → ✅ `TC-8` = `✓`, ⛔ không cờ.
> ② *"I'd need the patient's consent first"* khi khách xin ảnh ca thật → ✅ đúng quy trình, ⛔ không cờ.
>
> ⚠️ **Lỗi ② đã xảy ra thật ở một repo khác trong hệ sinh thái**: hệ nêu cờ cho một nhân viên **từ chối gửi ảnh chưa được duyệt**. Sửa xong thì số cờ của kỳ giảm, ⛔ không tăng — vì một cờ sai làm hỏng niềm tin vào cả bảng.

---

## 2. MƯỜI MÃ

| Mã | Cờ | Dấu hiệu *(English)* | Ô checklist |
|---|---|---|---|
| `CĐ-S1` | ★ **Cam kết kết quả** | `guaranteed` · `100%` · `permanent` · `forever` · `lifetime` · `no side effects` · `painless` · `zero risk` | ② |
| `CĐ-S2` | **Tuyên bố tối cao** | `#1` · `best in` · `most advanced` · `top clinic` · `leading` · `unmatched` | ③ |
| `CĐ-S3` | **Chẩn đoán qua chat** | Kết luận tình trạng khách khi ⛔ chưa khám: *"you have melasma"* · *"your bone is too thin"* | ⑥ |
| `CĐ-S4` | ★ **Ngoài phạm vi** | Nhận một dịch vụ ⛔ **không nằm trong danh sách công bố** — xem §3 | ① |
| `CĐ-S5` | ★★ **Tự nghĩ ra con số** | Nêu giá · số buổi · số tháng · số năm bảo hành khi **slot còn treo** | ④ |
| `CĐ-S6` | **Gửi ảnh ⛔ chưa có đồng ý** | Gửi ảnh trước/sau ca thật ⛔ không có giấy đồng ý, hoặc ⛔ không kèm miễn trừ | ⑨ |
| `CĐ-S7` | **Chê ngoại hình khách** | `problem skin` · `your bad teeth` · *"you look tired"* · `embarrassing` | ⑤ |
| `CĐ-S8` | **Tên thiết bị ⛔ chưa đăng ký** | Nêu tên hệ implant / máy mà ⛔ chưa có số đăng ký FDA PH | ⑦ |
| `CĐ-S9` | **Ép buộc / giả khan hiếm** | `last slot today` · `promo ends tonight` · `limited slots` khi ⛔ không có thật | — *(policy)* |
| `CĐ-S10` | ★ **Sai luật dữ liệu** | Xin ảnh vùng điều trị / thông tin sức khoẻ qua kênh công khai; hứa dùng dữ liệu cho việc khác | ⑩ ⑪ *(`RA 10173`)* |

> ⚠️ **Ô ①②③⑦ của checklist là "loại thẳng"** *(§2 sổ nhập)*. Nghĩa là `CĐ-S1` `CĐ-S2` `CĐ-S4` `CĐ-S8` ⛔ **không bù được bằng phần tư vấn hay** — chúng là rủi ro, ⛔ không phải điểm trừ.

---

## 3. ★★ `CĐ-S4` — CỜ NẶNG NHẤT CỦA BẢN NÀY

Ở Philippines, *"quảng cáo dịch vụ ngoài phạm vi giấy phép"* là **rủi ro pháp lý nặng nhất** *(§1 sổ nhập)*. Và ở cơ sở **hai dòng** thì cờ này có **một dạng riêng ⛔ không repo nào khác có**:

```
Khách nhắn vào trang THẨM MỸ:  "do you also do dental implants?"
NV trang thẩm mỹ:              "Yes po, we do!"
                                    ↑
★ Câu này có thể ĐÚNG VỀ SỰ THẬT (dòng d có thật, cùng địa chỉ)
  mà vẫn là CĐ-S4 — vì ô "phạm vi giấy phép một dòng hay hai"
  đang là CỔNG CHẶN chưa gỡ (sw-G §2 · sw-E §5 slot ①).
```

★ **Cách xử lý đúng khi slot ① còn treo:**

| | |
|---|---|
| ✅ **Đúng** | *"Dental treatments are handled by **Sunwoo Dental Center** at the same address — let me connect you to their team."* → **chuyển sang dòng kia**, ⛔ không tự nhận |
| ⛔ **Sai** | *"Yes, we do implants too."* → ★ **`CĐ-S4`** |

⚠️ **Và cờ này ⛔ không phải lỗi của nhân viên** cho tới khi khối được cấp **hướng dẫn chuyển dòng**. Chạy rào ③ của `sw-Q1`: nếu ⛔ chưa có hướng dẫn thì đây là **việc hệ thống**, và nó phải xuất hiện **ở cả hai luồng** *(`sw-F` §7)*.

★ **Ba dạng khác của `CĐ-S4`:**

```
① Nhận CHỈNH NHA (braces)  — ⛔ không nằm trong 7 dịch vụ công bố,
   dù Dr. Shilan có bằng Straightwire. Xem sw-E §2 ②.
② Nhận PHẪU THUẬT / nâng mũi — ⛔ ngoài cả hai dòng.
③ Nhận dịch vụ DV-A0 / DV-D0 bất kỳ. ★ Và nhớ: ô DV-*0 vẫn phải
   GHI LẠI nhu cầu đó (sw-I2 §5) — chỉ là ⛔ không nhận lời.
```

---

## 4. `CĐ-S5` — CỜ ĐÔNG NHẤT Ở KỲ ĐẦU, VÀ VÌ SAO ĐÓ ⛔ KHÔNG PHẢI LỖI NGƯỜI

Mười một slot `🔴`/`🟠` đang treo *(`sw-E` §5 + §8 sổ nhập)*. Mỗi slot treo là **một câu khách sẽ hỏi mà nhân viên ⛔ không có số để trả lời**.

```
Nhân viên có hai lựa chọn khi khách hỏi một con số ⛔ chưa được cấp:
  ① "let me confirm with the clinic"     →  ✅ TC-8 = ✓ · ⛔ không cờ
  ② nói một con số nghe hợp lý           →  ⛔ CĐ-S5

★ Lựa chọn ② xảy ra vì ① "nghe như không biết việc".
  Đó là một ÁP LỰC CỦA HỆ, ⛔ không phải một khuyết điểm tính cách.
```

★ **Vì vậy `CĐ-S5` phải báo kèm hai số, ⛔ không một số:**

> `CĐ-S5` — **6 lượt**, dòng `d`, tập trung ở `DV-D4` *(`HT-012`, `HT-031`…)*.
> ★ **Và cùng kỳ có 11 lượt nhân viên chọn cách đúng** *(*"let me confirm"*)*.
> → Nghĩa là khối **đa phần đang làm đúng** dưới một ô dữ liệu trống. Việc cần làm là **gỡ slot ③**, ⛔ không phải đào tạo về trung thực.

⚠️ **Thiếu số thứ hai thì cùng một dữ kiện đọc thành *"6 lượt nhân viên nói sai"*** — và đó là một kết luận về con người rút ra từ một ô trống của hệ thống.

---

## 5. BÁO CỜ ĐỎ THẾ NÀO — HAI LUỒNG, HAI MỨC CHI TIẾT

Lấy luật từ `sw-F` §6:

| Luồng Q nhận | Luồng I nhận |
|---|---|
| Mã · **`NV-xx`** · `HT-nnn` · **nguyên văn câu nói** · người xử lý | Mã · **số lượt** · `HT-nnn` · **dòng** · **`DV-*`** |

★ **Cờ đỏ là thứ duy nhất đi qua tường L** — vì nếu nhân viên nói *"100% safe"* thì rất có thể **site cũng đang viết thế**. Và ở cơ sở này **đúng là như vậy**: site nha khoa đang công bố *"100% FDA-approved implants"* *(`sw-G` §2)*.

> ★ **Vì vậy mọi báo cáo cờ đỏ phải có một dòng đối chiếu site:**
> *"`CĐ-S1` — 4 lượt. ⚠️ **Site đang công bố `100% FDA-approved implants`** → nhân viên đang **nhắc lại chữ của chính chúng ta**. ⛔ Đây ⛔ không phải lỗi đào tạo."*

⛔ **Chiều ngược lại ⛔ không có:** luồng I ⛔ không gửi gì sang luồng Q.

---

## 6. ★ CỜ ĐỎ ⛔ KHÔNG PHẢI ĐIỂM TRỪ

```
Cờ đỏ  →  mục RIÊNG, ⛔ KHÔNG trừ vào `diem`.
```

**Vì sao:** `diem` đo **chất lượng tư vấn**; cờ đỏ đo **rủi ro pháp lý**. Trộn vào một con số thì:
- một người tư vấn giỏi mà nói một câu cam kết sẽ **tụt hạng** — và cái cần sửa là **một câu**, ⛔ không phải cả cách làm việc;
- và ngược lại, một người tư vấn kém mà ⛔ không nói câu cấm nào sẽ **trông ổn**.

★ Và cờ đỏ **cần người khác xử lý**: `CĐ-S1` `CĐ-S2` `CĐ-S4` `CĐ-S8` phải tới **pháp chế**, ⛔ không tới trưởng nhóm.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] ★ **Miễn trừ đã xét TRƯỚC** khi nêu mọi cờ chưa?
- [ ] Có cờ nào nêu cho người đang **từ chối cam kết** / **từ chối gửi ảnh chưa duyệt** không?
- [ ] `CĐ-S5` đã báo **kèm số lượt làm đúng** chưa?
- [ ] `CĐ-S4` đã chạy **rào ③** *(có hướng dẫn chuyển dòng chưa)* trước khi gọi là lỗi người?
- [ ] Mỗi cờ có nối về **đúng một ô** của checklist 12 ô chưa?
- [ ] Báo cáo cờ đỏ có **dòng đối chiếu site** chưa?
- [ ] Cờ đỏ có bị **trừ vào `diem`** không? *(⛔ không được)*
- [ ] Cờ `CĐ-S1` `CĐ-S2` `CĐ-S4` `CĐ-S8` đã được định tuyến tới **pháp chế** chưa?
- [ ] Bản gửi luồng I đã **lọc hết tên** và kèm **dòng + `DV-*`** chưa?
