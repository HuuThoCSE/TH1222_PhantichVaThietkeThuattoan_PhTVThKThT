Cau 1, 2, 3

Xây dựng lớp SapXep_N^2

Selection Sort
- **Các giải thuật sắp xếp thứ tự nội (sắp xếp thứ tự trên mảng/dãy)**
- **Các giải thuật sắp xếp thứ tự ngoại (sắp xếp thứ tự trên tập tin)**


Insertion Sort
- **Thuật toán sắp xếp chèn trực tiếp (straight insertion sort)**

Đúng vậy, đoạn mã bạn đưa ra là một phiên bản của thuật toán sắp xếp chèn trực tiếp (Insertion Sort) trong Python. Thuật toán này hoạt động bằng cách duyệt qua danh sách từ trái sang phải, lấy từng phần tử và chèn nó vào đúng vị trí trong phần đã được sắp xếp phía bên trái của nó. Điều này được lặp lại cho đến khi danh sách được sắp xếp hoàn toàn.

Phương thức insertion_sort trong đoạn mã của bạn thực hiện thuật toán sắp xếp chèn trực tiếp như sau:

Duyệt từng phần tử trong danh sách bắt đầu từ vị trí thứ hai (vì phần tử đầu tiên được coi là đã sắp xếp).
Lưu giá trị của phần tử hiện tại vào biến X.
Tìm vị trí thích hợp (Pos) trong phần đã được sắp xếp để chèn phần tử hiện tại.
Di chuyển tất cả các phần tử lớn hơn X sang phải một vị trí.
Chèn phần tử X vào vị trí thích hợp (Pos).
Lặp lại bước 1-5 cho đến khi toàn bộ danh sách được sắp xếp.

- **Thuật toán sắp xếp chèn nhị phân (binary insertion sort)**

- Bubble Sort và cải tiến

Bubble Sort cải tiến (còn gọi là Cocktail Shaker Sort) là một biến thể của thuật toán Bubble Sort. Thuật toán này hoạt động bằng cách sắp xếp danh sách từ cả hai phía: từ trái sang phải và từ phải sang trái. Điều này giúp giảm thời gian sắp xếp đáng kể so với thuật toán Bubble Sort thông thường.

Hàm optimized_bubble_sort thực hiện Bubble Sort cải tiến như sau:

1. Đặt biến left và right là chỉ số bên trái và bên phải của phần chưa được sắp xếp.
2. Sắp xếp từ trái sang phải và cập nhật chỉ số phải của phần chưa được sắp xếp (right).
3. Sắp xếp từ phải sang trái và cập nhật chỉ số trái của phần chưa được sắp xếp (left).
4. Lặp lại bước 2-3 cho đến khi phần chưa được sắp xếp trở nên rỗng (left >= right).
Bạn có thể thay thế hàm bubble_sort hiện tại trong lớp Sapxep_NMu2 của bạn bằng hàm optimized_bubble_sort để tận dụng lợi ích của thuật toán Bubble Sort cải tiến.