# CHANGELOG

## v1.0 · 03/11/2026 — bản đầu

Agent đọc insight khách cho **Sunwoo Medical Center**, Philippines — **hai dòng dịch vụ**, **hai luồng đầu ra**, **hai tường ngăn**.

### Dựng

- 14 sổ `sw-A` … `sw-Q3` *(158.7 KB)*
- `SYSTEM-PROMPT.md` *(12.802)* · `SYSTEM-PROMPT-NGAN.md` *(7.931 — còn **69** dư)*
- `tools/sw.py` — `doc` · `insight --dong a|d` · `qc --dong a|d` · `kiem`
- `tools/tu_dien.json` — khớp **tiếng Anh** theo ranh giới từ
- 25 hội thoại mẫu *(English, cả hai dòng)* · 4 prompt
- `.gitignore` chặn `ma-nhan-vien.csv` **ngay từ commit đầu**

### Quyết định kiến trúc

**① HAI TƯỜNG, và chúng ⛔ không cùng loại.** Đây là điều khác mọi bản InsightDashboard trước.

| | **TƯỜNG D** *(dòng)* | **TƯỜNG L** *(luồng)* |
|---|---|---|
| Chặn | ⛔ Không **tỷ lệ** nào trộn mẫu số `a` + `d` | ⛔ Không **file** nào có cả tên NV và lời khách |
| Đơn vị | **Phép chia** | **Trường dữ liệu** |

★ Vì hai tường tác động lên **hai tầng khác nhau**, cấu trúc chỉ cần lồng **một lần** *(`a/d` × `i/q`)*, ⛔ không phải bốn file rời. Bốn file rời = bốn lần đọc = **bốn bộ số lệch nhau**.

**② TÁI DÙNG, ⛔ KHÔNG VIẾT LẠI.** `Agent-AdsOptimize-Phi` đã có **bốn sổ** về chính thương hiệu và chính thị trường này. Repo này **nhập** chúng và **sổ đó thắng** khi mâu thuẫn: vành đai `V1`–`V4` · nhóm `N1`–`N3` · phễu `S1`–`S6` · rào `SỢ·NGỜ·NGẠI·BỀN` · chân dung `CD1`–`CD6` · checklist 12 ô · `RA 10173`.

→ Mã **mới** chỉ đặt cho thứ ⛔ chưa có mã: `DV-A*`/`DV-D*` · **`SD1`–`SD6`** · **`LÂU`** · `CD-D*` · `TC-1`–`TC-10` · `CĐ-S1`–`CĐ-S10`.

**③ PHỄU DÒNG `d` VIẾT MỚI, ⛔ không tái dùng `S1`–`S6`.** Quyết định mua của implant khác **về bản chất**: một lần lớn · nhiều tháng chờ xương liền · kết quả gần vĩnh viễn. Rào thứ tư là **`LÂU`** *("bao lâu thì tôi có răng")*, ⛔ không phải **`BỀN`** *("năm sau còn trả bao nhiêu")*.

> ★ **Bằng chứng rằng `LÂU` là rào thật:** site của chính cơ sở đang bán vào đúng rào đó — *"2× faster bone integration"*. Họ **cược đúng chỗ**.

**④ `NGỜ` của dòng `d` xuất hiện HAI lần** — đầu phễu *("có nha sĩ thật không")* và **cuối phễu** *("hãng nào, ai cắm, bảo hành ra sao")*. Lần thứ hai mới là lần **mất ca đắt nhất**, vì khách đã chấp nhận giá rồi mới rơi.

**⑤ CỔNG G — cổng riêng của bản Philippines.** Cơ sở có **một chỗ**, khách phải đến tận nơi. `V0` ≥ 20% → ⛔ **DỪNG**. Vì *"nhóm này chốt kém"* mà ⛔ không biết họ ở đâu có thể chỉ là *"họ ở Quezon City và ⛔ không ai vượt EDSA 70 phút"*.

### ★ Phát hiện khi đọc hai site

**① Lỗi ② của sổ nhập ⛔ không được gỡ — nó chỉ ĐỔI CÂU HỎI.** Sổ nhập ghi *"FAQ nói có dental nhưng dịch vụ công bố chỉ là da liễu → xoá khỏi FAQ"*. Nay đã rõ dental là **dòng thật, có site riêng, cùng địa chỉ**. Nhưng câu hỏi mới vẫn là 🔴: **hai dòng nằm dưới một giấy phép hay hai?** Ở PH, *"quảng cáo dịch vụ ngoài phạm vi giấy phép"* là **rủi ro pháp lý nặng nhất**, nên ô này **giữ nguyên trạng thái cổng chặn**.

**② 🔴 Hotline hai site ⛔ không khớp — lệch bốn số cuối.**

```
sunwooaesthetic.ph : +63 9688858885  →  0968 885 8885
sunwoodental.ph    :  0968 885 8858  →  0968 885 8858
                                                 ↑↑↑↑
```

★ Một trong hai sai → **lead gọi vào ⛔ không tới ai**, và ⛔ không ai phát hiện vì người gọi ⛔ không gọi lại lần hai. **Ô rẻ nhất để gỡ và đắt nhất nếu bỏ qua** — chỉ cần gọi thử.

**③ Hai câu MẠNH NHẤT trên site nha khoa trả lời đúng hai rào quyết định — và ⛔ cả hai ⛔ không dùng được.** *"2× faster bone integration"* *(ô ④ — thiếu nguồn và thiếu mốc gốc)* và *"written warranty"* *(ô ② — cam kết kết quả)*. ★ Việc đáng làm ⛔ **không phải xoá**, mà là **làm cho chúng dùng được**.

**④ Tài sản mạnh nhất đang bị để chìm:** `Dr. Kay Dela Cruz`, D.M.D., **cắm implant từ 1999 — hơn 25 năm**. Ở một thị trường mà câu ngầm là *"năm năm nữa nó lung lay thì ai chịu"*, một con số **năm hành nghề** mạnh hơn mọi tính từ — và nó ⛔ **không cần ô dữ liệu nào mới**.

**⑤ `Dr. Shilan` có bằng Straightwire orthodontics, nhưng bảy dịch vụ công bố ⛔ không có chỉnh nha.** Có mà ⛔ không công bố = bỏ một dòng nhu cầu; ⛔ không có mà bằng cấp gợi ra = **đúng hình dạng của lỗi ②**.

### ⚠ Năm lỗi bắt được khi chạy thử

**① ★★ Khách QUAY LẠI bị gán nhãn PHẢN ÁNH.** Ban đầu `lam_o_dau == "tai-sunwoo"` **một mình** đủ để gắn nhãn *phản ánh*. Kết quả: `HT-025` — một khách **đã làm cleaning ở đây và nay hỏi veneer** — bị đọc thành một **ca khiếu nại**.

> ⚠️ Gán sai theo chiều này làm **mất ô `cheo`** — tài sản riêng của một cơ sở hai dòng — và biến **một ca bán thêm thành một ca khiếu nại**.
>
> → Sửa: thêm `gan_nhan_ht()`. `tai-sunwoo` + **dấu hiệu vấn đề** = `phan-anh`; `tai-sunwoo` + ⛔ không vấn đề = **`quay-lai`**. Và **biến chứng cấp tính sau một ca làm tại cơ sở là hậu mãi theo định nghĩa** → luôn `phan-anh`.

**② 🔴 `"your clinic"` bị đọc là *"tôi đã làm ở đây"*.** `HT-007` — *"Is your clinic HMO-accredited?"* — là một **khách mới đặt câu hỏi**, nhưng cụm `your clinic` nằm trong danh sách `tai_sunwoo` nên nó bị gán `tai-sunwoo`, rồi bị gán `quay-lai`.

> → Sửa: **cả hai** nhánh `tai-sunwoo` và `noi-khac` đều phải có **dấu hiệu "đã làm"** *(`had` · `got` · `months ago`…)*. Cùng họ với bài học *"nhận bằng LOGIC, ⛔ không bằng một cụm từ"*.

**③ ★★ Agent ĐOÁN DÒNG khi ⛔ không có dấu hiệu nào.** Mặc định ban đầu là `dong_hoi = ["a"]`. Nghĩa là mọi hội thoại ⛔ không nhắc dịch vụ nào bị **đẩy vào phễu dòng thẩm mỹ** — tức là vào **mẫu số của dòng đó**.

> ⚠️ **Đoán dòng là phá chính tường D**, và nó im lặng hoàn toàn: tổng vẫn khớp, mọi tỷ lệ vẫn tính được.
>
> → Sửa: ⛔ **không đoán**. Hội thoại ⛔ không có dấu hiệu dòng nào → vào `chua_ro_dong`, ⛔ **không vào phễu của dòng nào** — đúng như `V0` làm với vành đai. *(4/25 hội thoại mẫu nằm ở đây.)*

**④ Con số *"nhân viên chọn cách đúng"* bị thổi lên.** Nhãn ghi *"số lượt chọn cách đúng (`let me confirm`)"* nhưng công thức đếm `TC-8 == "✓"`, mà `TC-8` có nhánh mặc định *"có nói gì thì ✓"* → đếm ra **11/13**.

> ⚠️ Đây là một con số **dùng để bảo vệ khối** — thổi nó lên làm hỏng đúng cái lập luận nó phục vụ.
>
> → Sửa: lưu `noi_se_hoi` riêng và đếm trên nó. Số thật: **3/13** dòng `d`, **1/9** dòng `a`.

**⑤ `TC-5` cho `✓` miễn phí.** Logic ban đầu: ✗ nếu có tính từ trấn an, còn lại ✓. Nghĩa là **mọi câu trả lời bất kỳ** đều được ✓ ở ô *"trả lời bằng cơ chế/mốc"*.

> → Sửa: ba trạng thái — ✗ nếu tính từ trấn an · ✓ nếu **có mốc cụ thể** *(mốc thời gian, bước khám, phim, giờ mở, `let me confirm`)* · **`—` nếu ⛔ không rõ**. ★ `—` trung thực hơn một `✓` miễn phí, vì `—` ⛔ không vào mẫu số.

★ **Lỗi ① ② ③ cùng một họ:** cả ba đều là **đoán thay vì nói không biết**, cả ba **⛔ không gây lỗi chạy**, và cả ba cho ra bảng số **trông bình thường**.

### Đã kiểm

```
python tools/sw.py doc du-lieu/MAU_hoi-thoai.md --ky "28/10-02/11"
  → 25 HT phân biệt · a=10 · d=13 · chéo=2 · ⏸ chưa rõ dòng=4
  → ★ số học đúng: 10+13−2 = 21, +4 = 25
  → ⛔ CỔNG G CHẶN (V0 = 14/25 = 56%) — ★ đúng, mẫu thiếu dấu hiệu vùng
  → 3 nhân viên → NV-01…NV-03
insight --dong a|d · qc --dong a|d        → ✅ xuất đủ
kiem (cả 4 file)                          → ✅ CỔNG T qua
★ phép thử rò 13 kiểu                      → ✅ CHẶN đủ 13 (15/15 câu đúng)
```

Phép thử rò gồm cả hai tường: tên NV lọt vào `insight` · khoá `nv`/`diem` trong `insight` · khoá `cd`/`hook` trong `qc` · trích khách quá dài · **tỷ lệ ⛔ không nhãn dòng** · **mẫu số trộn** · **ô `cheo` lấy mẫu số một dòng** · SĐT · email · thiếu dòng khai mẫu · thiếu câu chân bảng.

### ⚠ Chưa có

- ⛔ **Chưa chạy trên hội thoại thật.** 25 hội thoại mẫu là **sinh ra**; tên nhân viên là tên giả.
- ⛔ **Chưa có bộ chân dung đã duyệt cho dòng nào** → **CỔNG 0** ở chế độ *phác lại mỗi kỳ*. `CD1`–`CD6` là **khuôn cho ads**; `CD-D1`–`CD-D6` là **giả thuyết kỳ đầu**.
- ⛔ **Bảy slot 🔴 đang treo** → **⛔ không viết được hook nào cho `SD4`**, chặng quyết định của dòng `d`. ⚠️ Repo **đọc được** và **đếm được** chỗ khách tắc, nhưng ⛔ không gỡ được — và trạng thái đó **trông như đang chạy**.
- ⛔ **Chỉ đọc tiếng Anh.** Taglish · Filipino · Hàn · Farsi ⛔ chưa đọc được, và mỗi thứ **lệch mẫu theo một hướng cụ thể** *(`sw-A` §7)* — nhóm `N1` gần như **biến mất** khỏi mọi báo cáo.
- ⛔ **Chưa có dashboard HTML.** Hiện chỉ xuất JSON + in ra console.

### ★ Ba va chạm mã — ⛔ không đổi tên

| Chữ | Ở repo này | Ở repo khác |
|---|---|---|
| `V` | **vành đai** `V1`–`V4` *(PH)* | `V-01`…`V-11` = **dịch vụ** *(Paris)* |
| `N` | **nhóm khách** `N1`–`N3` *(PH)* | `N1`–`N7` = **tiêu chí chấm** *(KNQT)* |
| `S` / `SD` | `S*` = chặng dòng `a` · `SD*` = chặng dòng `d` | — |

⛔ **Không nạp tri thức các repo này vào cùng project.** Quy ước: dịch vụ ở đây luôn viết `DV-A*`/`DV-D*`, tiêu chí luôn viết `TC-*`, và ⛔ **không viết `S4` khi nói về nha khoa**.
