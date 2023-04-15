import pandas as pd
import player

# Đọc file cleaned_player.csv
cleaned_player = pd.read_csv('cleaned_player.csv')

# Hàm được tạo để có thể gọi từ file .py khác như main.py chẳng hạn.
# Đầu vào là 1 player_list tạo sẵn hoặc không có gì cũng được.
# Lưu ý nếu player_list tạo sẵn thì số phần tử trong List cũng phải >= số cầu thủ (683)
# nếu không sẽ lỗi do đoạn code dưới chỉ gán giá trị chứ không tạo mới.
# Do vậy t nghĩ đoạn code này nên được chạy đầu tiên trước khi tạo variable, parameter
def set_player_list (player_list = None):
    # Nếu đầu vào không có gì thì player_list sẽ được tạo.
    if (player_list is None):
        # Ở đây tự khởi tạo số lượng object trong list tương đương với số cầu thủ.
        player_list = [None] * cleaned_player.shape[0]

    # Duyệt thông tin theo hàng.
    for index, row in cleaned_player.iterrows():
        # Tạo mới player, nên hàm init mới phải đúng đầu vào (18 cái).
        player_list[index] = player.Player(row[0], row[1], row[2], row[3], 
                                           row[4], row[5], row[6], row[7], 
                                           row[8], row[9], row[10], row[11], 
                                           row[12], row[13], row[14], row[15], 
                                           row[16], row[17], row[18])
    # Trả lại giá trị List để sử dụng.
    return player_list

# Test code.
if __name__ == "__main__":
    player_list_con = [None] * 683
    player_list = set_player_list(player_list_con)
    for i in range(25):
        player_list[i].print_all()