# sw-F · ★★ HAI TƯỜNG · CỔNG T

> Sổ này trả lời **một** câu: **cái gì được phép đi qua, và cái gì thì không.**
> ⛔ Chưa đọc hết §5 thì ⛔ không được xuất file nào.

---

## 1. TƯỜNG L · THEO LUỒNG — CHẶN LỌT TÊN

Hai luồng khác nhau ở **năm thứ cốt lõi**, mỗi thứ kéo theo một hệ quả kỹ thuật:

| | **LUỒNG I · INSIGHT KHÁCH** | **LUỒNG Q · QC TRỰC PAGE** |
|---|---|---|
| ① Chủ thể câu kết luận | *Khách* — "nhóm `CD-D2` đang vướng rào `LÂU`" | *Một con người* — "`NV-04` trượt `TC-4`" |
| ② Người đọc | Marketing · nội dung | Trưởng nhóm trực page · chính người đó |
| ③ Ngưỡng đủ mẫu | Theo **kỳ** *(≥50 mỗi dòng)* | Theo **người** *(≥10 HT)* |
| ④ Dữ liệu nhạy cảm | Lời khách → **ẩn danh khách** | Tên nhân viên → **che với người ngoài** |
| ⑤ Hệ quả khi sai | Hook sai → mất một tuần nội dung | ⚠️ Chấm sai → **mất một con người** |

### ★ Và thứ thứ sáu, nặng hơn cả năm cái trên

**Cùng một bằng chứng, hai luồng đọc ra hai nghĩa trái nhau.**

```
KH: how much for All-on-4?
NV: Hi po! May I have your number so our dentist can give you a quote?
KH: can you give a range first
NV: Let me confirm with the clinic and get back to you po.
```

| Luồng | Đọc ra | Việc phải làm |
|---|---|---|
| **I** | Khách vào từ post nói *"affordable full-arch"* rồi hỏi giá ngay → **post hứa giá mà trang đích ⛔ không có giá**. Đây là phát hiện về **nội dung** | Sửa post · thêm khung giá `DV-D4` |
| **Q** | Nhân viên **xin số trước khi hỏi tình trạng** → trượt `TC-3`. Nhưng *"let me confirm with the clinic"* ⛔ **không phải né giá** — ★ đó là **xử lý đúng** khi hệ chưa cấp giá | ⛔ **Không trừ `TC-9`.** Đẩy lên **việc hệ thống**: chưa cấp khung giá `DV-D4` |

> ⚠️ **Gộp hai luồng là ép người đọc chọn một trong hai nghĩa.** Và thực tế họ **luôn** chọn nghĩa của luồng Q — vì nó có tên người, nghe cụ thể hơn. Kết quả: lỗi nội dung và lỗi hệ thống bị ghi thành **lỗi nhân viên**, kỳ nào cũng vậy, và ⛔ không ai sửa post.

---

## 2. TƯỜNG D · THEO DÒNG — CHẶN TRỘN SỐ

Tường D ⛔ **không chặn trường dữ liệu** — nó chặn **phép chia**.

```
★ LUẬT: mọi tỷ lệ phải mang NHÃN DÒNG, và mẫu số phải nằm TRONG dòng đó.

✅  "dòng a · 18/52 hội thoại hỏi tổng liệu trình · 35%"
✅  "dòng d · 9/21 hội thoại hỏi thời gian · 43%"
✅  "chéo  · 6/73 hội thoại của kỳ hỏi cả hai dòng · 8%"

⛔  "35% hội thoại hỏi về chi phí"      ← dòng nào?
⛔  "tỷ lệ xin được số: 61%"            ← mẫu số trộn
⛔  "nhóm V2 chốt tốt hơn V3"           ← trộn hai quyết định mua khác nhau
```

### ★ Ba thứ đi qua tường D được

| Đi qua | Vì sao | ⛔ Nhưng |
|---|---|---|
| **Vành đai `V1`–`V4`** | Cùng quãng đường tới McKinley Hill | ⛔ Không gộp **tỷ lệ chốt** theo vành đai cho cả hai dòng |
| **Nhóm `N1`–`N3`** | Ba nhóm cắt ngang hai dòng | ⛔ Không kết luận về nhóm từ số trộn |
| ★ **Ô `cheo`** | Tài sản riêng của cơ sở hai dòng | Mẫu số là **tổng kỳ**, ⛔ không phải tổng một dòng |

### ⚠️ Mẫu số của ô `cheo` — chỗ dễ sai nhất của cả repo

```
6 hội thoại hỏi cả hai dòng.
Kỳ có 73 hội thoại: dòng a 52 · dòng d 21  (6 nằm trong CẢ HAI)

✅ ĐÚNG:  6 / 73  = 8%   ← mẫu số là TỔNG KỲ
⛔ SAI:   6 / 52  = 12%  ← "12% khách thẩm mỹ hỏi sang nha khoa"
⛔ SAI:   6 / 21  = 29%  ← "29% khách nha khoa hỏi sang thẩm mỹ"

★ Cùng SÁU hội thoại, ba con số. Cả ba trông hợp lý.
  Và 52 + 21 = 73 nên tổng VẪN KHỚP — ⛔ không ai phát hiện.
```

⚠️ Và vì 6 hội thoại nằm trong cả hai nhánh, **tổng hội thoại của kỳ ⛔ không bằng `len(a) + len(d)`**. Nó bằng **số `HT-nnn` phân biệt**. ⛔ Cộng hai nhánh lại là đếm 6 hội thoại hai lần.

---

## 3. ★ BẢNG THẨM QUYỀN — CỘT NÀO ĐI VÀO LUỒNG NÀO

| Cột bảng gốc | Luồng I | Luồng Q |
|---|---|---|
| `ht` *(`HT-nnn`)* | ✅ | ✅ | 
| `dong_hoi` *(`["a"]` / `["d"]` / `["a","d"]`)* | ✅ | ✅ |
| `dv` *(`DV-A*` / `DV-D*`)* | ✅ | ✅ |
| `chang` *(`S*` / `SD*`)* | ✅ | ⬜ |
| `rao` *(`SỢ`/`NGỜ`/`NGẠI`/`BỀN`/`LÂU`)* | ✅ | 🔶 chỉ để chấm `TC-4` |
| `vanh_dai` *(`V0`–`V4`)* · `nhom` *(`N1`–`N3`)* | ✅ | ✅ |
| `cd` *(chân dung)* | ✅ | ⛔ **KHÔNG** |
| `trich_khach` *(nguyên văn, đã ẩn danh)* | ✅ | 🔶 **chỉ cặp câu bằng chứng** |
| `cau_hoi_ngam` | ✅ | ⬜ |
| `lam_o_dau` · `an_toan` | ✅ | ✅ |
| `post_ads` | ✅ | ⬜ |
| **`nv`** *(tên / `NV-xx`)* | ⛔ **KHÔNG** | ✅ |
| `tc[1..10]` · `diem` · `loai` | ⛔ **KHÔNG** | ✅ |
| `co_do` | 🔶 **chỉ đếm tổng** | ✅ đầy đủ |
| `loi_he` | ✅ | ✅ |

Ký hiệu: ✅ đọc được · 🔶 có điều kiện · ⬜ không cần · ⛔ **bị chặn**

### ★ Luật cứng nhất

> **Cột `nv` ⛔ KHÔNG BAO GIỜ đi vào bất cứ đầu ra nào của luồng I.**
> ⛔ Không vào JSON, ⛔ không vào HTML, ⛔ không vào ghi chú, ⛔ không vào ví dụ minh hoạ.

Nếu một phát hiện insight **chỉ giải thích được bằng cách chỉ ra ai làm**, thì đó ⛔ **không phải phát hiện insight** — nó là phát hiện QC đặt sai chỗ.

| ⛔ Sai *(lọt tên)* | ✅ Đúng *(mức hiện tượng)* |
|---|---|
| *"`NV-04` trả lời 'implants last forever' — sai"* | *"Dòng `d`: 5/21 hội thoại được trả lời về độ bền bằng tính từ thay vì bằng T&C bảo hành (`HT-004`, `HT-019`…). ⚠ Site cũng đang công bố 'written warranty' mà ⛔ chưa có văn bản → **nhân viên đang nhắc lại chữ của chính chúng ta**."* |

> ⚠️ Bản đúng **mạnh hơn** bản sai. *"5/21 hội thoại"* là một vấn đề nội dung sửa được bằng một việc. *"`NV-04`"* là vấn đề của một người, và nó ⛔ không nói gì về 20 hội thoại còn lại.

---

## 4. ⛔ VÌ SAO ⛔ KHÔNG CÓ LỆNH `AUTO`

```
① AUTO sinh ra MỘT file. Một file thì ⛔ không có tường nào.

② Hai luồng có hai cổng khác nhau. AUTO phải dừng ở CỔNG 0 (của I)
   trong khi luồng Q đã sẵn sàng xong — tức là AUTO ép luồng Q
   CHỜ một cái duyệt ⛔ KHÔNG liên quan gì đến nó.

③ Hai luồng, hai người nhận, hai nhịp: insight theo nhịp nội dung,
   QC theo nhịp kèm cặp. Một lệnh ép hai nhịp thành một.

④ ★ Và ở bản này còn thêm: HAI DÒNG có hai nhịp nội dung khác nhau.
   Nội dung thẩm mỹ chạy theo tuần; nội dung implant chạy theo tháng
   vì chu kỳ quyết định của khách tính bằng tháng.
```

★ **Thay cho `AUTO`:** chạy `ĐỌC` **một lần**, rồi chạy `INSIGHT` và `QC` độc lập, **có tham số `--dong a` hoặc `--dong d`**, bao nhiêu lần cũng được. Tất cả đọc lại từ `out/doc-hoi-thoai.json` nên ⛔ không bao giờ lệch số.

---

## 5. ★★ CỔNG T — TÁM CÂU KIỂM, CHẠY BẰNG MÁY

⛔ Không file nào được xuất trước khi chạy đủ **tám câu**. Mỗi câu phải trả lời được bằng *"đã kiểm, kết quả là…"*, ⛔ không phải *"chắc là ổn"*.

```
── TƯỜNG L ──
① TÊN NHÂN VIÊN
   Tìm mọi tên trong bảng quy đổi, trên file sắp xuất của luồng I.
   Thấy dù một lần → ⛔ DỪNG. ⚠ Kiểm cả trong TÊN FILE và trong trích dẫn.

② FILE INSIGHT CÓ ĐIỂM SỐ KHÔNG
   Mọi khoá `nv` · `tc*` · `diem` · `loai` trong JSON insight
   → ⛔ phải KHÔNG TỒN TẠI. ⚠ Không phải "để rỗng" — phải KHÔNG CÓ KHOÁ.

③ FILE QC CÓ CHÂN DUNG / HOOK KHÔNG
   Khoá `cd` · `hook` · `ma_tran` · `ads` trong JSON qc → ⛔ phải KHÔNG CÓ.
   ★ Nhân viên ⛔ không được chấm bằng một thứ (chân dung của kỳ)
     mà họ ⛔ không hề biết khi đang trả lời khách.

④ FILE QC CÓ LỜI KHÁCH DÀI KHÔNG
   Trích khách trong báo cáo QC chỉ giữ ĐÚNG cặp câu làm bằng chứng
   cho ô ✗ đang xét. ⛔ Không chép cả hội thoại.

── TƯỜNG D ──
⑤ ★ TỶ LỆ CÓ NHÃN DÒNG CHƯA
   Mọi tỷ lệ trong mọi file → phải có `dong` = "a" | "d" | "ky".
   Thiếu nhãn → ⛔ DỪNG. ⚠ Đây là câu dễ trượt nhất.

⑥ ★ MẪU SỐ CÓ TRỘN KHÔNG
   Tỷ lệ nhãn "a" → mẫu số phải = n của dòng a.
   Tỷ lệ nhãn "d" → mẫu số phải = n của dòng d.
   Tỷ lệ nhãn "ky" → mẫu số phải = SỐ HT PHÂN BIỆT, ⛔ không phải n(a)+n(d).

── CHUNG ──
⑦ DỮ LIỆU KHÁCH & NHÓM MỎNG
   ⛔ Không SĐT · email · ảnh · link ở file nào, kể cả sổ tay riêng.
   Nhóm <10 HT → đã ẩn phần trăm chưa? Người <10 HT → đã bỏ phân loại chưa?
   Một `DV-*` chỉ 1–2 HT → có nhận ra được cá nhân không?

⑧ HAI DÒNG BẮT BUỘC
   · câu chân bảng của luồng Q:
     "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật
      hay xếp hạng công khai."
   · dòng khai mẫu (sw-A §7):
     "Mẫu kỳ này chỉ gồm hội thoại tiếng Anh. ⛔ Chưa đọc được:
      Taglish · Filipino · Hàn · Farsi."
```

⚠️ **Câu ①②③⑤⑥ phải làm bằng máy.** `tools/sw.py` có `kiem_tuong_ngan()` chạy đúng tám câu và **từ chối ghi file** *(`sys.exit(2)`)* nếu trượt. Chạy tay thì ⛔ **sẽ có kỳ quên** — và một tên lọt ra rồi thì ⛔ không gỡ lại được, báo cáo đã nằm trong hộp thư người khác.

---

## 6. CỜ ĐỎ — THỨ DUY NHẤT QUA TƯỜNG L, MỘT CHIỀU

Cờ đỏ pháp chế *(`sw-Q2`)* là **rủi ro pháp lý**, ⛔ không chỉ là lỗi tư vấn. Nó **phải tới được Marketing** — vì nếu nhân viên nói *"100% safe"* thì rất có thể **post ads cũng đang viết thế**, và ở Philippines đó là ô ② của checklist 12 ô.

| Luồng Q nhận | Luồng I nhận |
|---|---|
| Mã cờ · **ai** · `HT-nnn` · **nguyên văn câu nói** · người xử lý đích danh | Mã cờ · **số lượt** · `HT-nnn` · **dòng nào** · **`DV-*` nào hay bị** |

★ **Ví dụ đúng, luồng I:**
> `CĐ-S2` *(cam kết kết quả)* — **4 lượt**, dòng `d`, tập trung ở `DV-D5` veneer *(`HT-004`, `HT-019`, `HT-031`, `HT-052`)*. ⚠️ Rà lại site: trang đang công bố **"written warranty on veneers and crowns"** — nếu nội dung của chúng ta cam kết kết quả thì nhân viên **đang nhắc lại chữ của chính chúng ta**, và đây ⛔ **không phải lỗi đào tạo**.

⛔ **Chiều ngược lại ⛔ không có.** Luồng I ⛔ không gửi gì sang luồng Q.

---

## 7. VIỆC HỆ THỐNG — Ô GIAO NHAU CHÍNH ĐÁNG

Ô `✗` do **lỗi hệ** ⛔ không trừ điểm người, và **cả hai luồng đều phải thấy**:

| Lỗi hệ | Dòng | Luồng Q thấy | Luồng I thấy |
|---|---|---|---|
| ⛔ Chưa cấp **giá trọn gói / số buổi** | `a` | `TC-9` = `—` | *"Khách hỏi tổng liệu trình `n` lượt mà hệ ⛔ chưa có số"* → **thiếu nội dung `S4`** |
| ★ ⛔ Chưa cấp **thời gian & số lần hẹn** | `d` | `TC-9` = `—` | *"Khách hỏi `how long` `n` lượt"* → **thiếu nội dung `SD4`** |
| ⛔ Chưa cấp **tên hệ implant + số FDA PH** | `d` | Ô `—` khi khách hỏi hãng | *"Khách hỏi hãng `n` lượt"* → **`NGỜ` ② còn trống** |
| ⛔ Chưa có **T&C bảo hành văn bản** | cả hai | Ô `—` | *"Khách hỏi bảo hành `n` lượt"* → ⚠️ **site đang hứa mà ⛔ chưa có văn bản** |
| ★ ⛔ Chưa biết **có nhận HMO không** | `d` | Ô `—` | *"`n` lượt hỏi HMO"* → **mất nhóm `N2` ngồi ngay cạnh** |
| ⛔ Chưa có **case before–after có giấy đồng ý** | cả hai | Ô `—` khi khách xin ảnh | *"Khách xin ảnh `n` lượt"* → thiếu tài sản, ⚠️ và xem `sw-G` §3 |
| **Ngoài giờ** *(site ghi 9AM–6PM)* | cả hai | `TC-1` = `—` | *"Khách nhắn ngoài giờ `n` lượt"* → cân nhắc ca trực |

> ★ **Đây là giá trị lớn nhất của việc tách luồng.** Ở một báo cáo gộp, bảy dòng trên biến thành *"nhân viên né giá, ⛔ không nêu bảo hành"* — và khối trực page bị đào tạo về một việc **⛔ không phải lỗi của họ**, kỳ này qua kỳ khác.

⚠️ Mục *"việc hệ thống"* ⛔ **không được gộp vào mục "khuyến nghị"**. Nó phải là **mục riêng, có tên người chịu trách nhiệm cấp dữ kiện**.

---

## 8. BỐN CÁCH TƯỜNG BỊ PHÁ TRONG THỰC TẾ

```
① "CHO MỖI MỘT VÍ DỤ THÔI"
   Xin một ví dụ có tên người cho báo cáo insight "sinh động hơn".
   → ⛔ Không. Dùng HT-nnn. Mã hội thoại truy ngược được cho người
     CÓ QUYỀN truy ngược, và vô nghĩa với người không có. Đó là mục đích.

② "GỘP HAI FILE CHO DỄ GỬI"
   → ⛔ Không. Gửi hai file, hai người nhận.

③ "DASHBOARD CÓ Ô ĐĂNG NHẬP RỒI"
   → ⛔ Không trong bản này. Dashboard là file tĩnh, publish ra link;
     ai có link là mở được. Phân quyền bằng FILE, ⛔ không bằng màn hình.

④ ★ "CHO MỘT CON SỐ TỔNG CẢ PHÒNG KHÁM"
   Ai đó muốn một slide có MỘT tỷ lệ chốt cho cả cơ sở.
   → ⛔ Không. Đưa HAI con số kèm hai mẫu số. Nếu buổi họp cần một
     con số thì người chủ trì chọn — ⛔ không phải agent trộn hộ.
   ⚠️ Đây là cách tường D bị phá thường xuyên nhất, vì yêu cầu nghe
     rất hợp lý và người xin ⛔ không biết mình đang xin điều gì.
```

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Tám câu **CỔNG T** §5 đã chạy **bằng máy** chưa?
- [ ] File insight có **khoá** `nv`/`diem`/`loai`/`tc*` nào không? *(phải **không có khoá**, ⛔ không phải khoá rỗng)*
- [ ] File qc có khoá `cd`/`hook`/`ma_tran` nào không?
- [ ] ★ Mọi tỷ lệ đã có **nhãn dòng** chưa?
- [ ] ★ Tỷ lệ nhãn `ky` có lấy mẫu số là **số `HT` phân biệt** chứ ⛔ không phải `n(a)+n(d)`?
- [ ] Ô `cheo` có lấy mẫu số **tổng kỳ** chưa?
- [ ] Có phát hiện insight nào chỉ giải thích được bằng tên người không? → chuyển luồng Q
- [ ] Cờ đỏ sang luồng I đã **lọc hết tên** và đã kèm **dòng + `DV-*`** chưa?
- [ ] Mục **việc hệ thống** có ở **cả hai** báo cáo và có **tên người cấp** chưa?
- [ ] Hai dòng bắt buộc *(câu chân bảng + dòng khai mẫu tiếng Anh)* đã in chưa?
