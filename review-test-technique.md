1. Thiếu bước Requirement Analysis
   AC có Section 1 rất mạnh.
   TC thì lại vào luôn Happy Path.
   Theo mình nên có.
   Ví dụ

## 1. Analyse the requirement first

Before designing test cases, identify:

- Functional requirements
- Business rules
- Acceptance criteria
- Actors / roles
- Preconditions
- Triggers
- Expected outcomes
- State transitions
- External dependencies
- Assumptions

Lúc này AI sẽ biết phải đọc AC trước.

2. Positive / Happy Path
   Hiện

The main success scenario...

Mình sẽ sửa

Design at least one test case for every Happy Path acceptance criterion.

TC nên trace về AC.
Không nên trace về requirement.

3. Negative
   Thiếu một loại rất hay gặp.
   Ví dụ

Business rule violation

Ví dụ
Transfer

Daily limit exceeded

Recipient frozen

Currency not supported

Không phải invalid input.
Mà là business rule.
Nên thêm.

4. BVA + EP
   Rất chuẩn.
   Không sửa.

5. Field Validation
   Đây là chỗ mình muốn sửa.
   Hiện

from the screenshot

Nguy hiểm.
Có nhiều requirement
không có screenshot.
Mình sẽ sửa

For each user input defined by the requirement or visible in the UI.

AI sẽ không phụ thuộc screenshot.

6. UI / UX
   Tương tự.
   Hiện

from screenshot

Sửa thành

Where UI is provided.

7. Error & Resilience
   Ổn.

8. Edge
   Rất mạnh.
   Không sửa.

9. Non-functional
   Hay.
   Nhưng nên ghi

Include only when explicitly required or implied by the requirement.

Không thì AI sẽ generate
Performance Test
Accessibility
Localization
mọi lúc.

Prioritization
Đây là chỗ mình thích nhất.
Nhưng mình sẽ đổi.
Hiện

Assign each TC a priority.

Thành

Assign each TC a priority based on the Criticality of the acceptance criterion it verifies.

Vì guideline AC của mày vừa đổi sang Criticality.
Nó sẽ chain đẹp:
Requirement
↓
AC (Criticality)
↓
TC Priority

Coverage Rule
Hiện

Requirement -> TC

Theo mình chưa đủ.
Nên sửa

Coverage rule

Requirement → AC

AC → TC

Business Rule → TC

vì AI generate TC từ AC.
Không phải trực tiếp từ Requirement.

Thiếu một section rất lớn
Theo mình đây là thứ còn thiếu nhất.
Test Design Optimization
Ví dụ

Avoid redundant test cases.

Prefer combining compatible checks into one TC where they verify the same behaviour.

Split into multiple TC only when

- expected outcome differs
- preconditions differ
- business rule differs
- priority differs

AI rất hay generate
TC01
Recipient Name 1 char
TC02
Recipient Name 2 char
TC03
Recipient Name 3 char
...
rất phí.

Thiếu Traceability
Giống AC.
Nên thêm cuối.

Every test case shall reference

- Requirement ID
- AC ID
- Business Rule (if applicable)

Đây cực kỳ hữu ích.

Thiếu Review Checklist
AC có checklist.
TC cũng nên có.
Ví dụ

Final Check

✓ Every Critical AC covered

✓ Every Business Rule covered

✓ No duplicate TC

✓ Priority assigned

✓ Preconditions defined

✓ Expected Result objectively verifiable

✓ Traceable to AC

Chỗ duy nhất mình thấy không nên
Hiện

Skip one only when it genuinely does not apply

Mình sẽ đổi

Apply only the techniques that add meaningful coverage.
State explicitly when a technique is not applicable.

AI sẽ đỡ sinh TC cho đủ checklist.

Điểm mình chấm
Tiêu chí
Điểm
QA Test Design
10/10
AI Prompt
8.5/10
Enterprise
9/10
Traceability
8/10
Optimization
7.5/10
Kết luận
Nếu so với guideline AC thì mình thấy còn thiếu 3 mảnh ghép quan trọng:
1 Requirement/AC Analysis trước khi thiết kế TC (để AI hiểu đầu vào).
2 Traceability rõ ràng: Requirement → AC → TC (+ Business Rule → TC).
3 Test Design Optimization (tránh AI sinh hàng trăm TC trùng nhau).
Nếu bổ sung ba phần này, mình đánh giá guideline Test Design sẽ đạt chất lượng tương đương guideline AC của mày và rất phù hợp để AI sinh Test Cases một cách vừa đầy đủ vừa không bị "nổ số lượng".

Traceability rõ ràng: Requirement → AC → TC (+ Business Rule → TC). phần này tao muốn có những ticket nhỏ ko cần viết AC , đi thẳng từ requirement ra TCs luôn, m thấy hợp lý ko

Theo mình rất hợp lý, và thực tế nhiều team cũng làm vậy.
Điều mình không đồng ý chỉ là nếu guideline bắt buộc phải có AC trước mới được viết TC.
Mô hình linh hoạt sẽ tốt hơn.

Mình sẽ để Traceability như sau

Requirement
│
├──► Acceptance Criteria (recommended)
│ │
│ └──► Test Cases
│
└────────────────► Test Cases (when AC is intentionally omitted)

Nghĩa là:
• Ticket lớn → Requirement → AC → TC
• Ticket nhỏ → Requirement → TC

Mình sẽ sửa Coverage Rule
Thay vì

Requirement → AC

AC → TC

mình sẽ viết

Coverage rule

Every requirement shall be covered by one or more test cases.

Where acceptance criteria exist:

- Requirement → AC
- AC → TC

Where acceptance criteria are intentionally omitted:

- Requirement → TC

Every business rule shall be covered by at least one test case.

Như vậy AI sẽ tự hiểu:
• Có AC → trace từ AC.
• Không có AC → trace trực tiếp Requirement.

Thậm chí mình còn bổ sung vào đầu guideline
Ví dụ:

Acceptance Criteria are recommended for medium and complex requirements.

For simple, low-risk requirements, test cases may be designed directly from the requirement, provided full requirement coverage is maintained.

Đây là câu mình rất thích.
Nó phản ánh đúng thực tế:
• Ticket sửa typo → không cần AC.
• Đổi label → không cần AC.
• Thêm 1 field optional → có thể không cần AC.
• Thay đổi business flow → nên có AC.

Điều duy nhất mình sẽ yêu cầu
Dù có AC hay không thì Coverage Rule không đổi:

Requirement
↓
Covered?

Chỉ khác đường đi.
Có AC:

Requirement
↓
AC
↓
TC

Không AC:

Requirement
↓
TC

Miễn sao cuối cùng mọi requirement đều được ít nhất một TC kiểm chứng.

Theo mình đây là wording đẹp nhất

## Coverage rule

Every requirement must be covered by one or more test cases.

Where acceptance criteria are available, design test cases against the acceptance criteria.

Where acceptance criteria are intentionally omitted (e.g. simple or low-risk changes), design test cases directly from the requirement.

Every business rule must be verified by at least one test case.

Mình thích cách này vì nó không ép quy trình, nhưng vẫn giữ được traceability và phù hợp với cả ticket nhỏ lẫn ticket lớn.
