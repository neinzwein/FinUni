{-
Определите тип, представляющий геометрические фигуры на плос
кости. Фигура может быть либо окружностью (характеризуется
координатами центра и радиусом), прямоугольником (характери
зуется координатами верхнего левого и нижнего правого углов),
треугольником (координаты вершин) и текстовым полем (для него
необходимо хранить положение левого нижнего угла, шрифт и
строку, представляющую надпись). Шрифт задается из множества
трех возможных шрифтов: Courier, Lucida и Fixedsys. Определите
следующие функции.

-}
{-6 Функция move, по заданной фигуре и вектору сдвига возвращающая новую фигуру, сдвинутую относительно заданный на указанный вектор.
-}

data Font = Courier | Lucida | Fixedsys deriving (Show, Eq)

data Shape 
    = Circle (Double, Double) Double 
    | Rectangle (Double, Double) (Double, Double)
    | Triangle (Double, Double) (Double, Double) (Double, Double)
    | TextField (Double, Double) Font String
    deriving (Show, Eq)

move :: Shape -> (Double, Double) -> Shape
move (Circle (x, y) r) (dx, dy) = Circle (x + dx, y + dy) r
move (Rectangle (x1, y1) (x2, y2)) (dx, dy) = Rectangle (x1 + dx, y1 + dy) (x2 + dx, y2 + dy)
move (Triangle (x1, y1) (x2, y2) (x3, y3)) (dx, dy) = Triangle (x1 + dx, y1 + dy) (x2 + dx, y2 + dy) (x3 + dx, y3 + dy)
move (TextField (x, y) font text) (dx, dy) = TextField (x + dx, y + dy) font text

{-
move (Circle (0, 0) 5) (10, 15)
move (Rectangle (1, 2) (3, 4)) (2, 2)
move (Triangle (5.0,7.0) (7.0,5.0) (5.0,5.0)) (3,0)
-}
{-
move (TextField (1, 1) Courier "OnlyEng") (2, 3)
-}