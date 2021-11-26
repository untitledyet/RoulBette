# ფუნქციაში მოთავსებული კლასი, რომელსაც გადასცემ რიცხვს შემდეგი სახით (მაგ: Num1, Num2,Num3....Num N)
# და გიბრუნებს Dict_ს სადაც ამ რიცხვის დახასიათება წერია შემდეგი სახით   
# {'number': '22', 'color': 'black', 'odd_even': 'even', 'low_high': 'high', 'line': 'line1', 'sector': 'sector2'}


def ricxvis_agwera(NumX):
    class NumberDescription:
        def __init__(self, number, color, odd_even, low_high, col, sector):
                self.number = number
                self.color = color
                self.odd_even = odd_even
                self.low_high = low_high
                self.col = col
                self.sector = sector
        
    Num0 = NumberDescription("0", " ", " ", " ", " ", " ")
    Num1 = NumberDescription("1", "red", "odd", "low", "line1", "sector1")
    Num2 = NumberDescription("2", "black", "even", "low", "line2", "sector1")
    Num3 = NumberDescription("3", "red", "odd", "low", "line3", "sector1")
    Num4 = NumberDescription("4", "black", "even", "low", "line1", "sector1")
    Num5 = NumberDescription("5", "red", "odd", "low", "line2", "sector1")
    Num6 = NumberDescription("6", "black", "even", "low", "line3", "sector1")
    Num7 = NumberDescription("7", "red", "odd", "low", "line1", "sector1")
    Num8 = NumberDescription("8", "black", "even", "low", "line2", "sector1")
    Num9 = NumberDescription("9", "red", "odd", "low", "line3", "sector1")
    Num10 = NumberDescription("10", "black", "even", "low", "line1", "sector1")
    Num11 = NumberDescription("11", "black", "odd", "low", "line2", "sector1")
    Num12 = NumberDescription("12", "red", "even", "low", "line3", "sector1")
    Num13 = NumberDescription("13", "black", "odd", "low", "line1", "sector2")
    Num14 = NumberDescription("14", "red", "even", "low", "line2", "sector2")
    Num15 = NumberDescription("15", "black", "odd", "low", "line3", "sector2")
    Num16 = NumberDescription("16", "red", "even", "low", "line1", "sector2")
    Num17 = NumberDescription("17", "black", "odd", "low", "line2", "sector2")
    Num18 = NumberDescription("18", "red", "even", "low", "line3", "sector2")
    Num19 = NumberDescription("19", "red", "odd", "high", "line1", "sector2")
    Num20 = NumberDescription("20", "black", "even", "high", "line2", "sector2")
    Num21 = NumberDescription("21", "red", "odd", "high", "line3", "sector2")
    Num22 = NumberDescription("22", "black", "even", "high", "line1", "sector2")
    Num23 = NumberDescription("23", "red", "odd", "high", "line2", "sector2")
    Num24 = NumberDescription("24", "black", "even", "high", "line3", "sector2")
    Num25 = NumberDescription("25", "red", "odd", "high", "line1", "sector3")
    Num26 = NumberDescription("26", "black", "even", "high", "line2", "sector3")
    Num27 = NumberDescription("27", "red", "odd", "high", "line3", "sector3")
    Num28 = NumberDescription("28", "black", "even", "high", "line1", "sector3")
    Num29 = NumberDescription("29", "black", "odd", "high", "line2", "sector3")
    Num30 = NumberDescription("30", "red", "even", "high", "line3", "sector3")
    Num31 = NumberDescription("31", "black", "odd", "high", "line1", "sector3")
    Num32 = NumberDescription("32", "red", "even", "high", "line2", "sector3")
    Num33 = NumberDescription("33", "black", "odd", "high", "line3", "sector3")
    Num34 = NumberDescription("34", "red", "even", "high", "line1", "sector3")
    Num35 = NumberDescription("35", "black", "odd", "high", "line2", "sector3")
    Num36 = NumberDescription("36", "red", "even", "high", "line3", "sector3")

    return eval(NumX).__dict__

