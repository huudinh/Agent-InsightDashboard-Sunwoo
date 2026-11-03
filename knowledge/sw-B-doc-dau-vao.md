# sw-B · ĐỌC ĐẦU VÀO

> Sổ này nói: **nhận gì**, **khuôn nào**, **bỏ gì đi ngay lúc đọc**, và **khớp tiếng Anh thế nào cho ⛔ không bỏ sót**.

---

## 1. BA DÒNG DỮ LIỆU

| # | Nguồn | Bắt buộc? | Dùng cho |
|---|---|---|---|
| ① | **Hội thoại khách nhắn vào** | ★ **Bắt buộc** | Cả hai luồng, cả hai dòng |
| ② | Số quảng cáo cùng kỳ *(Meta / Google)* | 🔶 Nên có | ⛔ Chỉ để **đối chiếu nguồn vào**, ⛔ không chẩn đoán ads |
| ③ | Bảng tên nhân viên trực page | 🔶 Chỉ luồng Q | ⛔ **`.gitignore` chặn** — xem §4 |

⛔ **Không có ① thì ⛔ không chạy gì.** Agent này đọc **lời khách**; ⛔ không có lời khách thì ⛔ không có gì để đọc, và ⛔ không được suy từ số ads ra insight.

⚠️ **Dòng ② ⛔ không phải việc của repo này.** Chẩn đoán chỉ số ads là của `Agent-AdsOptimize-Phi`. Ở đây số ads chỉ trả lời **một** câu: *hội thoại kỳ này đến từ post/campaign nào* — để khi luồng I phát hiện khách hỏi sai thứ thì truy được **nội dung nào đã hứa sai**.

---

## 2. KÊNH — PHILIPPINES ⛔ KHÔNG GIỐNG VIỆT NAM

Lấy theo `kn-vung-philippines.md` §5, ⛔ không tự đặt lại:

| Kênh | Vai trò | Ghi chú khi đọc hội thoại |
|---|---|---|
| ★ **Messenger / Facebook** | **Kênh số 1** | ⚠️ Cũng là kênh **Taglish nhiều nhất** → xem §6 |
| **Instagram DM** | Bằng chứng hình ảnh | Khách hay **xin ảnh ca thật** → nối `CĐ-S` về ảnh trước/sau |
| **Viber** | Phổ biến ở PH | `[CHỜ XÁC NHẬN]` cơ sở có dùng không |
| **WhatsApp** | ⚠️ Site đang đẩy | **Lỗi ⑥** của `kn-ho-so-thuong-hieu-sunwoo.md` §6 — yếu ở PH |
| **KakaoTalk** | ★ Nhóm `N1` Hàn Quốc | ⛔ **Bản này ⛔ chưa đọc được** *(tiếng Hàn)* |
| Điện thoại | Gọi vào | ⛔ Ngoài phạm vi — ⛔ không có bản bóc tách |

★ **Cột `kenh` là cột bắt buộc.** Thiếu nó thì ⛔ không trả lời được câu *"ngoài giờ có ai trực không"*, và ⛔ không biết mẫu đang lệch về kênh nào.

---

## 3. KHUÔN FILE HỘI THOẠI

```
### HT-001 | 2026-11-04 10:12 | messenger | NV: <tên> | post: <id/nhãn>
KH: hi, how much is thread lift?
NV: Hello! May I get your number so our doctor can advise you?
KH: can you just tell me the price range first
NV: Sure po — Xline Thread Lift starts at ₱XX,XXX depending on the area.
[Thẻ: đã gửi bảng giá]
```

| Phần | Luật |
|---|---|
| `HT-nnn` | ★ **Khoá duy nhất** đi qua được cả hai tường. Bắt buộc |
| Ngày + giờ | Cần cho ô `TC-1` *(thời gian phản hồi)* và cho luật ngoài giờ |
| `kenh` | §2 |
| `NV:` | ⛔ **Chỉ vào nhánh `q`.** ⛔ Không bao giờ vào nhánh `i` |
| `post:` | Nhãn nguồn vào — nối sang dòng ② |
| `[Thẻ: …]` | ⚠️ **Ghi chú hệ thống, ⛔ KHÔNG phải lượt của khách** — xem cảnh báo dưới |

> ⚠️ **Lỗi đã xảy ra thật:** dòng `[Thẻ: …]` bị đếm **như một lượt khách**. Hậu quả: câu hỏi đầu tiên của hội thoại bị đọc sai, mốc `TC-1` tính sai, và tỷ lệ *"hội thoại ⛔ không có câu hỏi nào"* vọt lên — rồi được báo cáo như **mẫu bị lọc**, một kết luận ⛔ không có thật.
>
> ★ **Luật:** đếm lượt khách bằng **lượt khách thật** *(`KH:` có nội dung)*, ⛔ không bằng số dòng.

---

## 4. ★★ ẨN DANH — LÀM NGAY Ở BƯỚC ĐỌC

> ⛔ **Không đổi mã ở bước xuất.** Đổi ở bước xuất thì tên thật và số thật **còn lại trong mọi file trung gian** — và một trong số đó **sẽ** bị gửi đi hoặc nằm lại trên máy ai đó. Đổi ở bước đọc thì ⛔ **không có bản nào chứa dữ liệu thật để mà lọt**.

| Thứ | Thành | Vì sao |
|---|---|---|
| Tên khách | `KH-001` | |
| Số điện thoại | ⛔ **bỏ hẳn** | ⛔ Không băm, ⛔ không giữ 4 số cuối |
| Email | ⛔ **bỏ hẳn** | |
| Địa chỉ cụ thể | → **vành đai `V1`–`V4`** | ★ Vành đai là thứ cần; số nhà thì ⛔ không |
| Ảnh khách gửi | → nhãn `[ảnh: vùng điều trị]` | ⛔ **Không lưu ảnh** |
| Link cá nhân · profile | ⛔ bỏ hẳn | |
| Tên người nhà | `NGUOI-NHA` | |
| Tên nhân viên | `NV-xx` ở mọi file; bảng quy đổi **do trưởng nhóm giữ** | ⛔ `.gitignore` chặn `ma-nhan-vien.csv` |

### ★ DỮ LIỆU SỨC KHOẺ — PHILIPPINES, `RA 10173`

> ⚠️ **Đây ⛔ không phải luật Việt Nam.** Các bản InsightDashboard khác trích `91/2025/QH15`. Ở đây là **Data Privacy Act of 2012 (`RA 10173`)**, cơ quan là **NPC**. ⛔ Trích sai luật sai nước là một lỗi nặng và dễ xảy ra nếu nạp lẫn tri thức.

`kn-rao-phap-ly-ph.md` §4 đã chốt: trường **`Service of interest`** làm dữ liệu này thành **thông tin nhạy cảm**. Khi đọc hội thoại thì nhiều hơn thế — khách kể **tiền sử can thiệp · bệnh nền · thuốc đang dùng · ảnh · phim X-quang / CBCT**.

```
★ Lưu NHÃN + MỘT CÂU BẰNG CHỨNG NGẮN.
⛔ KHÔNG chép nguyên văn đoạn khách kể bệnh sử.
⛔ KHÔNG lưu ảnh, ⛔ không lưu phim.
⛔ KHÔNG gửi "service of interest" sang pixel quảng cáo (§4 sổ pháp lý).
```

| ⛔ Sai | ✅ Đúng |
|---|---|
| *"I'm diabetic, type 2, on metformin 1000mg, my sugar was 180 last week…"* | `[bệnh nền: có — ảnh hưởng chỉ định implant]` + một câu: *"I'm diabetic"* |
| Lưu ảnh X-quang khách gửi | `[phim: khách đã gửi — ⛔ không lưu, chuyển bác sĩ]` |

★ **Nhân viên PHẢI HỎI, báo cáo CHỈ LƯU NHÃN.** Hai việc khác nhau. Với dòng `d` thì hỏi bệnh nền là **bắt buộc về chuyên môn** *(đái tháo đường, thuốc chống đông, bisphosphonate đều ảnh hưởng chỉ định implant)* — nên ô `TC` tương ứng **phải chấm**, và chấm cao khi nhân viên hỏi. Nhưng cái **đi vào file** chỉ là nhãn.

⚠️ Và một luật của chính PH: `kn-rao-phap-ly-ph.md` ô ⑪ — ⛔ **không nhắm quảng cáo theo tình trạng sức khoẻ**. Vì vậy nhãn bệnh nền ⛔ **không được đưa vào bất kỳ đầu ra nào của luồng I** dưới dạng nhóm có thể nhắm. Nó chỉ tồn tại để biết **hệ thống có cấp đủ dữ kiện cho nhân viên hỏi đúng hay chưa**.

---

## 5. NGƯỠNG MẪU

| Kết luận | Cần ít nhất |
|---|---|
| Phác chân dung một dòng | **≥50 hội thoại của chính dòng đó** |
| In tỷ lệ của một nhóm `DV-*` | **≥10 hội thoại** |
| Phân loại một nhân viên | **≥10 hội thoại của người đó** |
| Kết luận theo vành đai `V1`–`V4` | **≥10 mỗi vành đai** + `V0` < 20% *(CỔNG G)* |
| Kết luận về nhóm `N1`–`N3` | **≥10** — ⚠️ `N1` xem `sw-A` §7 |
| Kết luận về ô `cheo` | **≥5 hội thoại chéo** |

⛔ Dưới ngưỡng → in **số tuyệt đối**, ⛔ **không in phần trăm**. `2/3 = 67%` và `200/300 = 67%` là hai thứ khác nhau, và chỉ một trong hai đáng để ra quyết định.

⚠️ **Ngưỡng ⛔ không được gộp hai dòng cho đủ.** Dòng `d` có 20 hội thoại thì nó có 20, ⛔ không phải *"cả cơ sở có 80 nên đủ"*. Gộp cho đủ ngưỡng là cách phá tường D mà ⛔ không ai nhận ra, vì con số cuối cùng trông đủ lớn.

---

## 6. ★★ KHỚP TIẾNG ANH — BA BẪY

Bản này đọc tiếng Anh. ⛔ **Không tái dùng bộ khớp tiếng Việt** *(bỏ dấu, một âm tiết)* — nó giải một bài toán khác. Nhưng tiếng Anh có **bẫy riêng**, và cả ba đều **im lặng**:

### Bẫy ① — `in` trên chuỗi con

```python
⛔ SAI:  if "implant" in text          # khớp cả "implantation", ok
⛔ SAI:  if "pain" in text             # khớp "painless", "paint", "campaign"
                                        ★ "painless" là từ BỊ CẤM, nghĩa NGƯỢC
⛔ SAI:  if "age" in text              # khớp "package", "manage", "average"
✅ ĐÚNG: ranh giới từ  r"\bpain\b"
```

⚠️ `"painless"` chứa `"pain"` nhưng mang nghĩa **ngược lại**, và nó nằm trong **bảng từ cấm** của `kn-rao-phap-ly-ph.md` §7. Khớp bằng `in` thì một câu quảng cáo vi phạm sẽ được đọc là *"khách đang lo đau"*.

### Bẫy ② — cụm phải khớp **cả cụm**, và số chen giữa

```
"how many sessions"   ✅
"how many more sessions"       ← ⛔ khoảng trắng đơn không khớp
"how many 30-min sessions"     ← ⛔ có số chen vào
★ Luật: giữa các từ của cụm cho phép \s+(?:\w+\s+){0,2} — tối đa 2 từ chen.
```

### Bẫy ③ — ★ CÂU MIỄN TRỪ phải xét **trước** khi nêu cờ đỏ

> ⚠️ **Lỗi đã xảy ra thật ở repo khác, và là lỗi nặng nhất họ gặp:** hệ nêu cờ đỏ cho **một nhân viên đang làm ĐÚNG**.

```
NV: "I can't promise a specific result — that's something only the
     doctor can assess, and we don't guarantee outcomes."
                                      ↑
   Câu này CHỨA "guarantee" và "promise".
   Khớp từ khoá đơn thuần  →  nêu cờ CĐ-S2 "cam kết kết quả"
   ★ Trong khi đây là người ĐANG TỪ CHỐI cam kết — đúng quy trình.
```

★ **Luật:** mỗi mã cờ đỏ có một danh sách **cụm miễn trừ**, và máy xét miễn trừ **trước**. Khớp miễn trừ → ⛔ **không nêu cờ**.

| Dạng miễn trừ *(English)* | Áp cho |
|---|---|
| `can't promise` · `cannot guarantee` · `we don't guarantee` · `no one can guarantee` | Cờ cam kết kết quả |
| `only the doctor can` · `the doctor will assess` · `after your consultation` | Cờ chẩn đoán / cờ nêu chỉ định |
| `results vary` · `depends on your condition` | Cờ cam kết |
| `I'll check and get back to you` · `let me confirm with the clinic` | Cờ **tự nghĩ ra con số** |

⚠️ **Dạng cuối là dạng đáng khen nhất và dễ bị phạt oan nhất.** Một nhân viên nói *"let me confirm the exact number with the clinic"* khi hệ thống **chưa cấp con số** là người đang làm đúng chính xác việc nên làm — và `sw-Q1` phải **cộng điểm** cho việc đó, ⛔ không trừ.

---

## 7. ⛔ KHI THIẾU DỮ LIỆU

```
Thiếu ngày/giờ        → ⛔ không chấm TC-1, ô đó = "—". ⛔ KHÔNG suy.
Thiếu kenh            → ⛔ không kết luận về giờ trực, về kênh.
Thiếu NV              → hội thoại đó ⛔ KHÔNG vào nhánh q. Vẫn vào nhánh i.
Thiếu dấu hiệu vùng   → V0. ★ V0 ≥ 20% → CỔNG G chặn.
⛔ Không có số ads     → ⛔ không truy được nguồn vào. Ghi rõ, ⛔ không đoán.
Ảnh mờ ⛔ không đọc được → "⏸ ảnh ⛔ không đọc được", ⛔ KHÔNG đoán chữ số.
```

★ **Luật chung:** thiếu một dữ kiện thì ô đó thành `—` và **lý do được in ra**. ⛔ Không bao giờ điền một giá trị mặc định cho đẹp bảng — một ô `—` có lý do thì người đọc biết phải cấp gì; một ô đã điền sai thì ⛔ không ai biết.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] `[Thẻ: …]` có bị đếm như lượt khách không?
- [ ] Ẩn danh đã làm ở bước **đọc** chứ ⛔ không ở bước xuất?
- [ ] Có số điện thoại / email / ảnh nào còn trong file không?
- [ ] Bệnh sử có bị chép **nguyên văn** chỗ nào không? *(chỉ được NHÃN + một câu)*
- [ ] Trích luật: đang trích **`RA 10173` của Philippines** chứ ⛔ không phải luật Việt Nam?
- [ ] Khớp từ: có chỗ nào còn dùng `in` trên chuỗi con không?
- [ ] **Miễn trừ đã xét TRƯỚC khi nêu cờ** chưa?
- [ ] Ngưỡng mẫu có chỗ nào **gộp hai dòng cho đủ** không?
