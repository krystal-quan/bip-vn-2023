import pandas as pd
import player as plr
import parameter as prm

# Hàm được tạo để có thể gọi từ file .py khác như main.py chẳng hạn.
# Đầu vào là 1 prm.playerList tạo sẵn hoặc không có gì cũng được.
# Lưu ý nếu prm.playerList tạo sẵn thì số phần tử trong List cũng phải >= số cầu thủ (683)
# nếu không sẽ lỗi do đoạn code dưới chỉ gán giá trị chứ không tạo mới.
# Do vậy t nghĩ đoạn code này nên được chạy đầu tiên trước khi tạo variable, parameter
def set_player_list (playerList = None):
    # Đọc file cleaned_player.csv
    cleaned_player = pd.read_csv('cleaned_player.csv')
    # Nếu đầu vào không có gì thì prm.playerList sẽ được tạo.
    if (playerList is None):
        # Ở đây tự khởi tạo số lượng object trong list tương đương với số cầu thủ.
        playerList = [None] * cleaned_player.shape[0]

    # Duyệt thông tin theo hàng.
    for index, row in cleaned_player.iterrows():
        # Tạo mới player, nên hàm init mới phải đúng đầu vào (18 cái).
        playerList[index] = plr.Player(index + 1, row[0], row[1], row[2], row[3], 
                                           row[4], row[5], row[6], row[7], 
                                           row[8], row[9], row[10], row[11], 
                                           row[12], row[13], row[14], row[15], 
                                           row[16], row[17], row[18])
    prm.TOTAL_PLAYERS = len(playerList)
    # Trả lại giá trị List để sử dụng.
    return playerList
    