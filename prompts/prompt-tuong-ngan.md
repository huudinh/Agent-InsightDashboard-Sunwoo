# Prompt · `CỔNG T` — kiểm **hai tường** trước khi xuất

> ⛔ Không file nào được xuất trước khi chạy đủ **tám câu**. Năm câu đầu chạy **bằng máy**, ⛔ không bằng mắt.

---

```
CỔNG T — kiểm hai tường cho <tên file>.

── TƯỜNG L · chặn LỌT TÊN ──
① TÊN NHÂN VIÊN
   Tìm mọi tên trong bảng quy đổi, trên file luồng I sắp xuất.
   Thấy dù một lần → ⛔ DỪNG.
   ⚠ Kiểm cả trong TÊN FILE và trong trích dẫn.

② FILE INSIGHT CÓ ĐIỂM SỐ KHÔNG
   Khoá `nv` · `tc*` · `diem` · `loai` → ⛔ phải KHÔNG TỒN TẠI.
   ⚠ ⛔ Không phải "để rỗng" — phải KHÔNG CÓ KHOÁ ĐÓ.

③ FILE QC CÓ CHÂN DUNG / HOOK KHÔNG
   Khoá `cd` · `hook` · `ma_tran` · `ads` → ⛔ phải KHÔNG CÓ.
   ★ Nhân viên ⛔ không được chấm bằng một thứ (chân dung của kỳ) mà
     họ ⛔ KHÔNG HỀ BIẾT khi đang trả lời khách.

④ FILE QC CÓ LỜI KHÁCH DÀI KHÔNG
   Chỉ giữ ĐÚNG cặp câu làm bằng chứng cho ô ✗ đang xét.
   ⛔ Không chép cả hội thoại.

── TƯỜNG D · chặn TRỘN SỐ ──
⑤ ★ TỶ LỆ CÓ NHÃN DÒNG CHƯA
   Mọi tỷ lệ phải có `dong` = "a" | "d" | "ky". Thiếu → ⛔ DỪNG.
   ⚠ Đây là câu DỄ TRƯỢT NHẤT.

⑥ ★ MẪU SỐ CÓ TRỘN KHÔNG
   nhãn "a"  → mẫu số = n(a)
   nhãn "d"  → mẫu số = n(d)
   nhãn "ky" → mẫu số = SỐ HT PHÂN BIỆT, ⛔ KHÔNG phải n(a)+n(d)

── CHUNG ──
⑦ DỮ LIỆU KHÁCH & NHÓM MỎNG
   ⛔ Không SĐT · email · ảnh · link ở file nào, kể cả sổ tay riêng.
   Nhóm <10 HT → đã ẩn phần trăm chưa?
   Người <10 HT → đã bỏ phân loại chưa?
   Một DV-* chỉ 1–2 HT → có nhận ra được cá nhân không?

⑧ HAI DÒNG BẮT BUỘC
   · câu chân bảng của luồng Q:
     "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay
      xếp hạng công khai."
   · dòng khai mẫu:
     "Mẫu kỳ này chỉ gồm hội thoại tiếng Anh. ⛔ Chưa đọc được:
      Taglish · Filipino · Hàn · Farsi."
```

---

```bash
python tools/sw.py kiem out/insight-d.json
python tools/sw.py kiem out/qc-d.json --ma-nv ma-nhan-vien.csv
```

★ Hàm `kiem_tuong_ngan()` chạy đúng tám câu trên, và **mọi lần ghi JSON đều đi qua `ghi_json()`** — ⛔ không ghi trực tiếp ở chỗ khác. Trượt thì **từ chối ghi** *(`sys.exit(2)`)*, ⛔ không chỉ cảnh báo.

⚠️ **Chạy tay thì ⛔ sẽ có kỳ quên.** Và một tên lọt ra rồi thì ⛔ **không gỡ lại được** — báo cáo đã nằm trong hộp thư người khác.

---

## Ai được xem file nào

| File | Publish? | Người nhận |
|---|---|---|
| `out/doc-hoi-thoai.json` | ⛔ **Không** — chứa nhánh `q` | ⛔ Chỉ máy đọc |
| `out/insight-a.json` · `-d.json` | ✅ sau CỔNG T | Marketing |
| `out/dashboard-i-*.html` | ✅ sau CỔNG T | Marketing |
| `out/qc-*.json` · `dashboard-q-*.html` | ⛔ **Không** | Trưởng nhóm |
| `out/so-tay-NV-xx.md` | ⛔ **Không** | ⛔ **Chỉ người đó** |

> ⚠️ **File gốc ⛔ không được gửi đi, dù tên nó nghe như một file tạm.** Nó là file **dễ bị gửi nhất** chính vì vậy.

---

## ⛔ Bốn cách tường bị phá

```
① "CHO MỖI MỘT VÍ DỤ THÔI"
   Xin một ví dụ có tên người cho báo cáo insight "sinh động hơn".
   → ⛔ Không. Dùng HT-nnn — truy ngược được cho người CÓ QUYỀN truy
     ngược, và vô nghĩa với người không có. Đó chính là mục đích.

② "GỘP HAI FILE CHO DỄ GỬI"  → ⛔ Không. Hai file, hai người nhận.

③ "DASHBOARD CÓ Ô ĐĂNG NHẬP RỒI"
   → ⛔ Không trong bản này. Dashboard là file tĩnh, ai có link là mở
     được. Phân quyền bằng FILE, ⛔ không bằng màn hình.

④ ★ "CHO MỘT CON SỐ TỔNG CẢ PHÒNG KHÁM"
   → ⛔ Không. Đưa HAI con số kèm HAI mẫu số. Buổi họp cần một con số
     thì NGƯỜI CHỦ TRÌ chọn — ⛔ không phải agent trộn hộ.
   ⚠ Đây là cách tường D bị phá THƯỜNG XUYÊN NHẤT, vì yêu cầu nghe
     rất hợp lý và người xin ⛔ KHÔNG BIẾT mình đang xin điều gì.
```

---

## ⛔ Lọc và gộp — ⛔ không ra quyết định

```
Agent đưa số, bằng chứng và câu thay thế. NGƯỜI THẬT KÝ.

⛔ Không đề xuất kỷ luật · cắt thưởng · xếp hạng công khai · cho nghỉ.
⛔ Không kết luận về CON NGƯỜI — chỉ về VIỆC và về Ô.
```

★ Một bản chấm của máy dùng làm căn cứ kỷ luật là cách nhanh nhất để cả khối **thôi tin vào nó** — và khi họ thôi tin thì **dữ liệu đầu vào hỏng theo**: hội thoại được trả lời cho đẹp bảng chấm chứ ⛔ không cho khách. Lúc đó agent mất **thứ duy nhất nó có**.
