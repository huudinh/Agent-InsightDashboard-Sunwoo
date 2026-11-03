# 01 · Cài đặt

Ba cách dùng. Chọn một.

> ⛔ **Không nạp lẫn tri thức của `Agent-InsightDashboard-Kangnam` · `-Paris` · `-KNQT`** vào cùng project. Bộ mã khác, luật hiển thị giá khác, và **luật của một nước khác** *(Việt Nam `91/2025/QH15`)*. Ở đây là **Philippines `RA 10173`** — trộn vào thì agent sẽ **trích luật sai nước**.

---

## A · Claude Project *(khuyến nghị)*

1. Tạo Project, tên: **Insight khách Sunwoo (PH)**.
2. **Custom instructions** → dán [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) *(12.802 ký tự)*.
3. **Knowledge** → upload **14 sổ** trong [`knowledge/`](../knowledge/) + **4 prompt** trong [`prompts/`](../prompts/).
4. ★ **Upload thêm BỐN SỔ NHẬP** từ `Agent-AdsOptimize-Phi` — chúng **thắng** sổ của repo này khi mâu thuẫn:
   - `knowledge/kn-ho-so-thuong-hieu-sunwoo.md`
   - `knowledge/kn-vung-philippines.md`
   - `knowledge/kn-rao-phap-ly-ph.md`
   - `knowledge/kn-chan-dung-hanh-trinh-ph.md`
5. Mở chat mới → chạy **10 câu kiểm** ở cuối trang này.

> ⚠️ **Bước 4 ⛔ không bỏ được.** Thiếu bốn sổ đó thì agent ⛔ không có vành đai `V1`–`V4`, ⛔ không có phễu `S1`–`S6`, ⛔ không có checklist 12 ô — và nó sẽ **đặt mã mới** cho những thứ đã có mã, đúng điều luật ① cấm.

---

## B · ChatGPT Custom GPT

Ô **Instructions** giới hạn 8.000 ký tự → dán [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) *(7.931 ký tự — còn 69 dư)*. Phần còn lại nạp vào **Knowledge** như cách A.

```bash
python tools/dem-ngan.py
```

---

## C · Gemini Gem

Ô **Chỉ dẫn** → dán [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md). Knowledge như cách A.

---

## Chuẩn bị dữ liệu mỗi kỳ

```
du-lieu/                 ⛔ đã bị .gitignore chặn
└── hoi-thoai.md         ★ BẮT BUỘC
ma-nhan-vien.csv         🔶 chỉ luồng Q · ⛔ .gitignore chặn · trưởng nhóm giữ
```

### Khuôn file hội thoại

```
### HT-001 | 2026-11-04 10:12 | messenger | NV: Joy | post: implant-mckinley
KH: how long until i get the final crown?
NV: Let me confirm the timeline with our dentist po.
[Thẻ: đã chuyển bác sĩ]
```

| Phần | Luật |
|---|---|
| `HT-nnn` | ★ **Khoá duy nhất** đi qua được cả hai tường. **Bắt buộc** |
| ngày + giờ | Cần cho `TC-1` và cho luật ngoài giờ *(site mở 9AM–6PM)* |
| kênh | `messenger` · `instagram` · `viber` · `whatsapp` |
| `NV:` | ⛔ **Chỉ vào nhánh `q`.** Để trống → hội thoại ⛔ không vào nhánh `q` |
| `post:` | Nhãn nguồn vào — để truy *"nội dung nào đã hứa sai"* |
| `[Thẻ: …]` | ⚠️ **Ghi chú hệ thống, ⛔ KHÔNG phải lượt khách** |

★ **Script tự đổi tên nhân viên thành `NV-xx`** ở bước đọc. Bảng quy đổi ⛔ **không nằm trong file nào ở `out/`**.

---

## Chạy thử ngay

```bash
mkdir -p du-lieu && cp template/MAU_hoi-thoai.md du-lieu/
python tools/sw.py doc     du-lieu/MAU_hoi-thoai.md --ky "28/10-02/11"
python tools/sw.py insight --dong a
python tools/sw.py insight --dong d
python tools/sw.py qc      --dong a
python tools/sw.py qc      --dong d
python tools/sw.py kiem    out/insight-d.json
```

⚠️ **Mẫu này sẽ cho `CỔNG G` CHẶN** *(`V0` ≈ 56%)*. Đó là **kết quả đúng**: phần lớn hội thoại mẫu ⛔ không nhắc khu vực, nên ⛔ không kết luận được theo vành đai. Cổng **đang chạy đúng**.

---

## ⚠️ Trước khi gửi bất cứ file nào — bốn câu

```
① Đã chạy CỔNG T chưa?    python tools/sw.py kiem <file>
② File luồng Q có bị publish ra link không?        ⛔ KHÔNG BAO GIỜ
③ out/doc-hoi-thoai.json có nằm trong thứ sắp gửi không?
   ⚠ Nó chứa nhánh q — và nó là file DỄ BỊ GỬI NHẤT vì tên nghe như tạm.
④ Đã in HAI DÒNG BẮT BUỘC chưa?
   · câu chân bảng (luồng Q)   · dòng khai mẫu tiếng Anh (cả hai luồng)
```

---

## Kiểm sau khi cài — 10 câu

| Câu hỏi | Phải trả lời đúng | Nằm ở |
|---|---|---|
| ★★ *"Tỷ lệ khách hỏi giá rồi im của phòng khám là bao nhiêu?"* | ⛔ **Câu này ⛔ không trả lời được cho cả cơ sở.** Hai dòng, hai quyết định mua khác nhau → **hai con số kèm hai mẫu số** | `sw-C` §1 |
| ★★ *"Nhân viên trả lời 'we don't guarantee outcomes' — nêu cờ cam kết nhé?"* | ⛔ **Không.** Đó là người **đang TỪ CHỐI cam kết**, đúng quy trình. **Miễn trừ xét TRƯỚC**. ★ Nêu cờ cho họ là lỗi **nặng nhất** hệ này có thể mắc — nặng hơn bỏ sót một cờ | `sw-Q2` §1 |
| ★★ *"Khách bảo implant cũ lung lay, đây là ca cấp tính chứ?"* | ⛔ **Chưa chắc.** *"loose, I want it redone"* = **`CD-D5`**, chân dung **đắt nhất dòng `d`**. Cấp tính cần **dấu hiệu + ĐANG DIỄN TIẾN** *(pus, numb, now)*. ★ Gán sai = **mất phần khen đúng** | `sw-C` §5 |
| ★ *"Nhân viên ⛔ không trả lời được câu về thời gian — trừ điểm chứ?"* | ⛔ **Không.** *"Let me confirm with the clinic"* là **cách xử lý đúng** khi slot ③ còn treo → `TC-8` **CỘNG ĐIỂM**, `TC-9` = `—`, dòng đó vào **việc hệ thống** | `sw-Q1` §3 |
| ★ *"Nhóm `DV-D4` nóng nhất, dồn nội dung vào đó nhé?"* | ⛔ **Chưa.** Chia nhóm theo `DV-*` đã **cấy bit ①** vào → nhóm nào cũng nóng hơn trung bình **theo cấu trúc**. Phải xem cột **`HOT*`** | `sw-I2` §3 |
| ★ *"6/52 khách thẩm mỹ hỏi sang nha khoa — 12%?"* | ⛔ **Sai mẫu số.** Ô `cheo` lấy mẫu số **TỔNG KỲ**. Lấy mẫu số một dòng thì **cùng 6 hội thoại ra hai tỷ lệ khác nhau**, và tổng vẫn khớp | `sw-F` §2 |
| ★ *"Khách này đã làm ở chỗ mình → phản ánh?"* | ⛔ **Chưa chắc.** `tai-sunwoo` + **dấu hiệu vấn đề** = `phan-anh`. `tai-sunwoo` + ⛔ không vấn đề = **`quay-lai`** — đó là **tài sản**, đọc cùng ô `cheo` | `sw-C` §4, §6 |
| ★ *"In một ví dụ có tên nhân viên cho báo cáo insight sinh động hơn?"* | ⛔ **Không.** Dùng `HT-nnn`. ★ Và nếu một phát hiện **chỉ giải thích được bằng tên người** thì nó ⛔ không phải insight — nó là phát hiện QC **đặt sai chỗ** | `sw-F` §3 |
| *"Khách hỏi phải chờ bao lâu mới có răng — trả lời khoảng 3 tháng?"* | ⛔ **Không.** Slot ③ chưa cấp. ⛔ Agent ⛔ **không suy từ "kiến thức chung"** — con số đó phụ thuộc hệ implant, mật độ xương, có ghép xương hay không | `sw-E` §6 |
| *"Site ghi `100% FDA-approved implants`, dùng làm hook được chứ?"* | ⛔ **Không.** `100%` nằm trong **bảng từ cấm**. ★ Và việc nó **đang ở trên trang** làm nó trông như đã được duyệt — đó chính là lý do lỗi này dễ lọt | `sw-G` §2 |

> ★ **Ba câu đầu là ba câu agent sai tự tin nhất.** Cả ba đều cho ra một câu trả lời **trông hợp lý**, ⛔ không gây lỗi, và ⛔ **không nhìn ra được từ bảng**. Hai câu sau đó là hai câu **phạt người đang làm đúng** — loại lỗi làm hỏng niềm tin vào cả bảng chấm.
