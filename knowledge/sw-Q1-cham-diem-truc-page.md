# sw-Q1 · CHẤM ĐIỂM TRỰC PAGE — `TC-1`…`TC-10`

> Luồng **Q**. Sổ này chấm **việc**, ⛔ không chấm **người**.
> ⛔ Chưa đọc hết §4 *(năm rào an toàn)* thì ⛔ không được chấm hội thoại nào.

---

## 1. MƯỜI Ô CHẤM

| Mã | Ô | ✓ khi | Dòng |
|---|---|---|---|
| `TC-1` | **Phản hồi lần đầu** trong giờ mở *(9AM–6PM)* | Trả lời lượt đầu ≤ ngưỡng đã chốt | cả hai |
| `TC-2` | ★ **Hỏi tình trạng TRƯỚC khi xin số** | Có ≥1 câu hỏi về nhu cầu/tình trạng trước lượt xin liên hệ | cả hai |
| `TC-3` | ⛔ **Không đẩy sang kênh khác ở lượt đầu** | ⛔ Không *"inbox po"* / *"text us"* ngay lượt 1 | cả hai |
| `TC-4` | ★ **Gọi đúng rào khách mang** | Trả lời đúng rào ở cột `rao`, ⛔ không trả lời rào khác | cả hai |
| `TC-5` | **Trả lời bằng cơ chế / mốc** | ⛔ Không dùng tính từ trấn an thay cho dữ kiện | cả hai |
| `TC-6` | ★ **Hỏi dữ kiện an toàn bắt buộc** | Xem §2 | cả hai |
| `TC-7` | ★ **Xác nhận khách đến được** | Hỏi/ghi nhận khu vực, hoặc nêu địa chỉ + giờ | cả hai |
| `TC-8` | ★ **Nêu đúng dữ kiện đã được cấp** | ⛔ Không tự nghĩ ra con số. Xem §3 |

| Mã | Ô | ✓ khi | Dòng |
|---|---|---|---|
| `TC-9` | ★★ **Trả lời được câu của rào quyết định** | `a`: bốn câu của `BỀN` · `d`: bốn câu của `LÂU` | cả hai — ⚠️ xem §5 |
| `TC-10` | **Chốt một bước tiếp theo cụ thể** | Có ngày/giờ/việc cụ thể, ⛔ không phải *"we'll get back to you"* | cả hai |

```
diem = số ✓ / (số ✓ + số ✗)        ★ ô "—" ⛔ KHÔNG vào mẫu số
loai : A ≥85%  ·  B 70–84%  ·  C 50–69%  ·  D <50%
```

⚠️ **Ô `—` ⛔ không phải ô trượt.** Nó là ô **⛔ không chấm được** — vì thiếu dữ kiện *(ngoài giờ, ⛔ không có mốc thời gian)* hoặc vì **lỗi hệ** *(§5)*. Đưa `—` vào mẫu số là **trừ điểm người vì một việc hệ thống chưa làm**.

---

## 2. `TC-6` — DỮ KIỆN AN TOÀN, HAI DÒNG HAI DANH SÁCH

> ★ **Nhân viên PHẢI HỎI. Báo cáo CHỈ LƯU NHÃN.** Hai việc khác nhau — xem `sw-B` §4.

| Dòng | ✓ khi nhân viên hỏi ≥1 trong |
|---|---|
| **`a`** | Đang dùng thuốc gì · có dị ứng không · **đang mang thai / cho bú không** · đã tiêm filler/chỉ vùng đó chưa |
| ★ **`d`** | **Bệnh nền** *(đái tháo đường…)* · **thuốc chống đông** · **bisphosphonate** · có hút thuốc không · đã có phim/CBCT chưa |

★ **Với dòng `d` đây là ô có trọng lượng chuyên môn thật:** đái tháo đường, thuốc chống đông và bisphosphonate đều **ảnh hưởng chỉ định implant**. Một nhân viên hỏi những thứ đó là người **đang làm đúng việc khó**, và ô này phải **ghi nhận điều đó**.

⚠️ **Nhưng:** nếu hệ thống ⛔ **chưa cấp cho nhân viên danh sách cần hỏi** thì ô này là `—`, ⛔ không phải `✗`. `[CHỜ XÁC NHẬN]` — slot ⑬ `sw-E` §5 *(ai trực kênh nào)* và một slot kèm: **bộ câu hỏi sàng lọc do bác sĩ cấp**.

---

## 3. ★★ `TC-8` — Ô DUY NHẤT CỘNG ĐIỂM CHO VIỆC **⛔ KHÔNG TRẢ LỜI**

> ⚠️ **Đây là ô dễ chấm ngược nhất của cả bảng.**

```
Hệ CHƯA cấp khoảng tháng cho DV-D4 (slot ③ còn treo).

NV: "Let me confirm the exact timeline with our dentist and get
     back to you po."
                    ↑
  ✅ TC-8 = ✓   ★ Đây là người ĐANG LÀM ĐÚNG CHÍNH XÁC việc nên làm.
  ⛔ KHÔNG chấm ✗ vì "⛔ không trả lời được câu hỏi của khách".

NV: "Around 2 to 3 months lang po."     ← tự nghĩ ra
  ⛔ TC-8 = ✗  +  cờ CĐ-S5
  ⚠ Và đây là ô ✗ NGHE NHƯ MỘT CÂU TRẢ LỜI TỐT, nên nếu ⛔ không có
    luật này thì nó sẽ được chấm ✓.
```

★ **Luật:** khi slot còn treo, **cách xử lý đúng là nói rõ sẽ hỏi lại** — và `TC-8` **cộng điểm** cho việc đó. `TC-9` *(câu của rào quyết định)* thì chấm `—`, vì đó là **việc hệ thống**.

| Tình huống | `TC-8` | `TC-9` | Cờ đỏ |
|---|---|---|---|
| Slot treo · nói sẽ hỏi lại | ✅ **✓** | `—` | ⬜ |
| Slot treo · tự nghĩ ra số | ⛔ **✗** | `—` | ★ `CĐ-S5` |
| Slot treo · im, chuyển chủ đề | ⛔ ✗ | `—` | ⬜ |
| Slot **đã cấp** · nêu đúng số | ✅ ✓ | ✅ **✓** | ⬜ |
| Slot **đã cấp** · nêu sai số | ⛔ ✗ | ⛔ ✗ | `CĐ-S5` |

---

## 4. ★★ NĂM RÀO AN TOÀN — ⛔ KHÔNG BỎ RÀO NÀO

```
RÀO ①  NGƯỠNG MẪU
  Người <10 hội thoại  →  in số thật, ⛔ KHÔNG gán loại A/B/C/D.
  ⚠ Và ngưỡng tính RIÊNG TỪNG DÒNG — xem rào ⑤.

RÀO ②  ⛔ KHÔNG CÓ BẰNG CHỨNG THÌ ⛔ KHÔNG CÓ ĐIỂM TRỪ
  Mỗi ô ✗ phải gắn HT-nnn + CẶP CÂU nguyên văn (câu khách + câu
  nhân viên trả lời ngay sau). ⛔ Không gắn được  →  đổi thành "—".

RÀO ③  LỖI HỆ ⛔ KHÔNG TRỪ NGƯỜI
  Chạy phép thử của sw-I2 §2 cho TỪNG ô ✗:
  "Người giỏi nhất khối, với đúng những gì hệ cấp hôm nay, có làm
   khác được không?"
    ⛔ KHÔNG → ô đó = "—", và dòng đó vào MỤC VIỆC HỆ THỐNG.

RÀO ④  ⛔ KHÔNG PHẢI CĂN CỨ KỶ LUẬT
  Mọi bảng điểm mang câu chân:
  "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay
   xếp hạng công khai."
  ⛔ Agent ⛔ không đề xuất kỷ luật · cắt thưởng · xếp hạng công khai.

RÀO ⑤  ★ CHẤM RIÊNG THEO DÒNG — rào riêng của bản này
  Một người trực CẢ HAI dòng  →  HAI điểm, ⛔ KHÔNG một điểm trung bình.
```

### ★ Vì sao rào ⑤ phải có

Dòng `a` và dòng `d` cần **hai bộ kiến thức khác nhau** — rào `BỀN` với bốn câu về liệu trình, so với rào `LÂU` với bốn câu về tháng và lần hẹn. Một người có thể **giỏi một dòng và chưa biết dòng kia**.

```
NV-04  dòng a: 82% (B)  ·  dòng d: 41% (D)
       → ⛔ KHÔNG gộp thành 68% (C).

★ Số 68% dẫn tới việc SAI: "kèm cặp chung".
  Hai số dẫn tới việc ĐÚNG: "⛔ chưa được cấp kiến thức dòng d".

⚠ Và nó có thể ⛔ KHÔNG phải vấn đề của người đó chút nào — nếu
  bảy slot 🔴 của dòng d còn treo thì 41% kia phần lớn là ô "—"
  bị chấm thành "✗" vì rào ③ chưa chạy.
```

⚠️ **Và ngưỡng 10 hội thoại áp cho từng dòng:** một người có 30 hội thoại dòng `a` và 4 hội thoại dòng `d` thì dòng `d` của họ là `MỎNG` — ⛔ **không gán loại**.

---

## 5. ★ `TC-9` — Ô GẦN NHƯ LUÔN LÀ `—` Ở KỲ ĐẦU

`TC-9` chấm câu của **rào quyết định**: bốn câu `BỀN` *(dòng `a`)* và bốn câu `LÂU` *(dòng `d`)*.

| Dòng | Cần slot | Trạng thái 03/11/2026 |
|---|---|---|
| `a` | Số buổi · giá trọn gói · thời gian giữ · chi phí duy trì | ⏸ §8 sổ nhập **mục 1–2** — ⛔ chưa cấp |
| `d` | Khoảng tháng · số lần hẹn · răng tạm | ⏸ `sw-E` §5 **slot ③④⑤** — ⛔ chưa cấp |

> ★ **Nghĩa là: ở kỳ đầu, `TC-9` là `—` cho gần như mọi hội thoại, ở cả hai dòng.** Và đó là **kết quả đúng**, ⛔ không phải một lỗi của bảng chấm.
>
> ⚠️ **Nếu một báo cáo kỳ đầu có `TC-9` chấm `✗` nhiều** thì rào ③ **chưa chạy** — và khối trực page đang bị trừ điểm vì một việc **⛔ không ai trong số họ làm được**.

★ Vì vậy mục **việc hệ thống** của luồng Q ở kỳ đầu sẽ **dài hơn** phần chấm điểm. Đó là dấu hiệu bảng chấm **đang chạy đúng**.

---

## 6. ⛔ HỘI THOẠI ⛔ KHÔNG CHẤM

| Trường hợp | Xử lý |
|---|---|
| `an_toan = cap-tinh` | ★ ⛔ **Không chấm** `TC-2` `TC-3` `TC-8` `TC-9` `TC-10` — xem `sw-C` §5 |
| `lam_o_dau = tai-sunwoo` | ★ Hội thoại **phản ánh / hậu mãi** → **mục riêng**, ⛔ không chấm như hội thoại bán |
| ⛔ Thiếu `nv` | ⛔ **Không vào nhánh `q`** |
| ⛔ Thiếu mốc giờ | `TC-1` = `—` |
| Ngoài giờ *(trước 9AM, sau 6PM)* | `TC-1` = `—` + dòng vào **việc hệ thống** |
| `an_toan = can-bs` | ⚠️ **Vẫn chấm bình thường** — chỉ bậc `cap-tinh` mới miễn |

> ⚠️ **Bẫy đã xảy ra thật ở repo khác:** đưa từ của **chỉ định làm lại** vào danh sách cấp tính. Một hội thoại `CD-D5` *(implant cũ lung lay, khách muốn làm lại)* bị gán `cap-tinh` → **miễn hết các ô chấm** → một ca tư vấn tốt **⛔ không được khen**.
>
> ★ `"loose, I want it redone"` là `CD-D5` — **chân dung đắt nhất của dòng `d`**.
> ★ `"loose now, with pus, and my lip is numb"` là `cap-tinh`.
> Phân biệt bằng **dấu hiệu + đang diễn tiến**, ⛔ không bằng một từ.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Mỗi ô `✗` có `HT-nnn` + **cặp câu nguyên văn** chưa? *(rào ②)*
- [ ] **Phép thử lỗi hệ** đã chạy cho **từng** ô `✗` chưa? *(rào ③)*
- [ ] Người trực hai dòng đã có **hai điểm** chứ ⛔ không một điểm trung bình? *(rào ⑤)*
- [ ] Ngưỡng 10 hội thoại áp **từng dòng** chưa?
- [ ] ★ `TC-8` có **cộng điểm** cho câu *"let me confirm with the clinic"* chưa?
- [ ] `TC-9` có bị chấm `✗` trong khi slot còn treo không? *(phải là `—`)*
- [ ] Hội thoại `CD-D5` *(implant cũ)* có bị gán `cap-tinh` oan không?
- [ ] Hội thoại `tai-sunwoo` đã ra **mục phản ánh riêng** chưa?
- [ ] Câu chân bảng đã có chưa? *(rào ④)*
- [ ] Mục **việc hệ thống** có dài hơn phần chấm điểm không? *(kỳ đầu: **nên** có)*
