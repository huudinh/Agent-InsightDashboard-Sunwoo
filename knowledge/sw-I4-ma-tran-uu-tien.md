# sw-I4 · MA TRẬN ƯU TIÊN · CỔNG 1

> Luồng **I**, bước cuối. Sổ này trả lời: **kỳ tới làm gì trước**, và **⛔ đừng xếp thứ tự bằng cái gì**.

---

## 1. ★★ XẾP THEO **SỐ HỘI THOẠI ẢNH HƯỞNG**, ⛔ KHÔNG THEO TỶ LỆ XẤU NHẤT

```
Nhóm A: 3/4 hội thoại rơi ở rào X   →  75%  →  ảnh hưởng  3 hội thoại
Nhóm B: 18/52 rơi ở rào Y           →  35%  →  ảnh hưởng 18 hội thoại

★ SỬA NHÓM B TRƯỚC, dù 35% nhìn "đỡ" hơn 75% rất nhiều.
```

⚠️ **Tỷ lệ xấu nhất gần như luôn thuộc nhóm nhỏ nhất** — vì nhóm nhỏ thì một hội thoại đã là 25%. Xếp theo tỷ lệ là xếp theo **độ nhỏ của mẫu**, ⛔ không theo độ nặng của vấn đề.

★ **Và `n < 10` thì ⛔ không in tỷ lệ gì cả** *(`sw-B` §5)* — nên nhóm đó **⛔ không vào được ma trận** bằng tỷ lệ. Nó vào bằng **số tuyệt đối**, ở một dòng riêng có nhãn `MỎNG`.

### ⛔ Và ⛔ không quy ra tiền bằng một giá trị đơn tự đặt

```
⛔ "18 hội thoại × ₱80,000 = ₱1.44M mất"

Giá trị đơn là slot ⑧ của §8 sổ nhập và slot ⑨ của sw-E §5 — CHƯA CẤP.
Một con số tiền SAI thì nó QUYẾT SAI THỨ TỰ SỬA, và nó thuyết phục
hơn con số đúng vì nó có đơn vị tiền.

★ Chưa có giá trị đơn → xếp theo SỐ HỘI THOẠI, và NÓI RÕ đã xếp
  theo cách đó.
```

⚠️ **Ngoại lệ duy nhất, và nó ⛔ không phải tiền:** khi so **giữa hai dòng**, được phép ghi *"`DV-D4` là dịch vụ giá trị ca cao nhất cả cơ sở"* vì đó là **dữ kiện đã biết** *(`sw-C` §3)*, ⛔ không phải một con số tự đặt. Nhưng đó là một **ghi chú kèm**, ⛔ không phải trục xếp hạng.

---

## 2. HAI TRỤC CỦA MA TRẬN

| | **Làm được ngay** | ⏸ **Chặn bởi slot** |
|---|---|---|
| **Ảnh hưởng nhiều** | ★ **Ô ①** — làm kỳ này | ★ **Ô ②** — **đi hỏi, ⛔ không viết** |
| **Ảnh hưởng ít** | Ô ③ — làm nếu còn chỗ | Ô ④ — ghi lại, ⛔ không làm |

### ★ Ô ② là ô quan trọng nhất của bản này

⚠️ **Kỳ đầu của dòng `d` sẽ có phần lớn phát hiện nằm ở ô ②**, vì **bảy slot 🔴** đang treo *(`sw-E` §5)*. Và việc đúng cho ô ② ⛔ **không phải là viết nội dung** — nó là **một email hỏi một câu**.

```
★ Việc của ô ② ghi thành:
  "⏸ CẤP DỮ KIỆN: khoảng tháng từ cắm đến răng cuối, theo từng DV-D*
   → Bác sĩ  ·  chặn: chặng SD4, 9/21 hội thoại dòng d
   ★ Gỡ ô này gỡ luôn bốn hook (sw-I3 §3) và một micro-conversion."

⛔ KHÔNG ghi thành "viết nội dung về timeline implant" — ⛔ không viết
  được, và ghi thế thì kỳ sau nó xuất hiện lại nguyên văn.
```

> ★ **Một báo cáo kỳ đầu mà ô ① đầy và ô ② trống là một báo cáo đã tự điền slot.** Nếu agent viết được hook cho `SD4` mà slot ③④⑤ chưa cấp thì nó **đã nghĩ ra một con số** — xem cờ `CĐ-S5`.

---

## 3. ★ `HOT*` LÀ ĐIỀU KIỆN VÀO MA TRẬN

⛔ **Bảng so độ nóng ⛔ không có cột `HOT*` thì ⛔ không được dùng để xếp ưu tiên.** Xem `sw-I2` §3.

| Nhóm | n | `HOT` | ★ `HOT*` | Đọc ra |
|---|---|---|---|---|
| `DV-D4` All-on-4 | 9 | 4.1 | **2.1** | Nóng thật, nhưng ⛔ không nóng như `HOT` tưởng — bit ① bị cấy |
| `SD4` | 9 | 4.3 | **1.9** | ⚠️ `HOT` cao **theo định nghĩa** của chặng *(bit ②③)* |
| `V1` lõi | 14 | 3.8 | **2.8** | ★ **Chênh ít nhất → nóng thật nhất** |

★ **Đọc đúng bảng này: cột đáng tin là `HOT*`, và cái đáng chú ý là KHOẢNG CHÊNH.** Chênh lớn = độ nóng phần lớn **do cách chia nhóm**, ⛔ không do khách.

⚠️ Riêng nhóm **chân dung** `cd` bỏ **ba** bit *(①②③)* nên `HOT*` của nó luôn thấp — ⛔ **đừng so `HOT*` của chân dung với `HOT*` của vành đai**. So trong **cùng một cách chia nhóm**.

---

## 4. ★ BA NHỊP — ⛔ ĐỪNG DỒN MỌI VIỆC VÀO MỘT KỲ

Hai dòng có **hai nhịp quyết định khác nhau**, nên ⛔ không xếp chung một lịch:

| Nhịp | Dòng `a` | Dòng `d` |
|---|---|---|
| **Nhịp 1 · trong kỳ** | Sửa câu trả lời sai · thêm mục vào trang | Như `a` |
| **Nhịp 2 · 2–4 tuần** | Viết tuyến nội dung `S3`/`S4` | Viết tuyến `SD3` |
| ★ **Nhịp 3 · 1–3 tháng** | Liệu trình · bảng giá trọn gói | ★ **Toàn bộ `SD4`** — vì nó cần **bác sĩ chốt quy trình**, ⛔ không chỉ cần viết |

> ★ **Chu kỳ quyết định của khách dòng `d` tính bằng tháng**, ⛔ không bằng tuần: khách đọc về implant hôm nay có thể quyết định sau Giáng sinh. Vì vậy **⛔ không đo hiệu quả nội dung `d` theo tuần** — và ⛔ không kết luận *"tuyến nội dung implant ⛔ không hiệu quả"* sau hai tuần.
>
> ⚠️ Và mùa vụ PH làm điều này rõ hơn: `kn-vung-philippines.md` §7 — **tháng 11 đến đầu tháng 1** là cao điểm *(tiệc cuối năm, OFW về, 13th-month pay)*. Nội dung `SD4` muốn kịp mùa đó phải bắt đầu **từ tháng 10**.

---

## 5. CỔNG 1 — AGENT DỪNG Ở ĐÂU

```
Agent in ma trận  →  ⏸ DỪNG  →  người chọn làm gì kỳ này

⛔ Agent ⛔ KHÔNG tự chọn.
⛔ Agent ⛔ KHÔNG gộp hai dòng vào một danh sách việc.
★ In HAI ma trận, một cho mỗi dòng, cộng MỘT mục "việc hệ thống"
  dùng chung (vì nhiều slot chặn cả hai dòng).
```

★ **Và in thêm một dòng cuối, bắt buộc:**

> *"Ma trận này xếp theo **số hội thoại ảnh hưởng**, ⛔ không theo tỷ lệ và ⛔ không quy ra tiền *(⛔ chưa có giá trị đơn)*. Mẫu kỳ này **chỉ gồm hội thoại tiếng Anh** — ⛔ chưa đọc được Taglish · Filipino · Hàn · Farsi, nên ⛔ không kết luận về nhóm `N1` và số của `V3` có thể đang **đọc thiếu**."*

---

## 6. KHUÔN MỘT DÒNG MA TRẬN

```
① ⏸ CẤP DỮ KIỆN: khoảng tháng cắm → răng cuối, theo từng DV-D*

   Ô            : ② (ảnh hưởng nhiều · chặn bởi slot)
   DÒNG         : d
   ẢNH HƯỞNG    : 9/21 hội thoại dòng d  (⚠ n=21, in kèm mẫu số)
   HOT*         : 1.9  (HOT 4.3 — ★ chênh 2.4, phần lớn do cách chia nhóm)
   RÀO          : LÂU
   CHÂN DUNG    : CD-D1 [PHÁC] · CD-D2 [PHÁC · MỎNG n=7]
   NGƯỜI NHẬN   : ★ Bác sĩ   —   hạn: <ngày>
   GỠ LUÔN      : 4 hook (sw-I3 §3) + 1 micro-conversion + ô TC-9 luồng Q
   NHỊP         : 3 (1–3 tháng)
   ⛔ KHÔNG LÀM : ⛔ không viết nội dung timeline trước khi có ô này
```

**Ba thứ bắt buộc:** **người nhận có tên** · **mẫu số in kèm** · ★ **ô "gỡ luôn"**.

> ★ **Ô "gỡ luôn" là ô làm cho việc được ưu tiên thật.** Một slot gỡ được **bốn hook, một micro-conversion và một ô chấm** thì nó ⛔ không còn là *"một câu hỏi cho bác sĩ"* — nó là việc đáng làm nhất của kỳ. ⚠️ Thiếu ô này thì mọi dòng ⏸ trông như nhau và ⛔ không ai biết hỏi câu nào trước.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Xếp theo **số hội thoại ảnh hưởng** chứ ⛔ không theo tỷ lệ?
- [ ] Có chỗ nào **quy ra tiền** bằng giá trị đơn tự đặt không?
- [ ] Mọi bảng độ nóng có cột **`HOT*`** chưa? Có so `HOT*` **chéo cách chia nhóm** không?
- [ ] Việc ở ô ② đã ghi thành ⏸ **"cấp dữ kiện + ai cấp"** chứ ⛔ không ghi thành *"viết nội dung"*?
- [ ] Mỗi dòng ma trận có **người nhận có tên** và ô **"gỡ luôn"** chưa?
- [ ] Mẫu số đã in kèm mọi tỷ lệ chưa? Nhóm `MỎNG` đã in **số tuyệt đối** chưa?
- [ ] In **hai** ma trận *(một cho mỗi dòng)* + **một** mục việc hệ thống chứ ⛔ không gộp một?
- [ ] Dòng khai cuối *(xếp theo gì · mẫu chỉ tiếng Anh)* đã in chưa?
