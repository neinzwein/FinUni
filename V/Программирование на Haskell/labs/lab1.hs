{---1----}
{-
1) ((Char,Integer), String, [Double])
let a = (('a',1),"abc",[1.0])
2) [(Double,Bool,(String,Integer))]
-}

a = [(1.0,True,("abc",1))]
{-:t a-}

{-
3) ([Integer],[Double],[(Bool,Char)])
4) [[[(Integer,Bool)]]]
-}
b = [[[(1,True)]]]
{-:t b-}

5) (((Char,Char),Char),[String])
6) (([Double],[Bool]),[Integer])
7) [Integer, (Integer,[Bool])]
8) (Bool,([Bool],[Integer]))
9) [([Bool],[Double])]
10) [([Integer],[Char])]
max3 :: Integer-> Integer -> Integer ->Integer

max3 a b c = max a $ max b c

min3 :: Integer-> Integer -> Integer -> Integer

min3 a b c = min a ( min b c )

sort2 :: Integer-> Integer->(Integer,Integer)

sort2 a b = if a>b then (b, a) else (a,b)

bothTrue :: Bool -> Bool -> Bool

bothTrue a b = if a==b then (if a==True then True else False) else False

solve2 :: Double -> Double ->(Bool, Double)

solve2 a b = if a==0 then (if b==0 then (True,0.0) else (False,0.0)) else (if b==0 then (False,0.0) else (True,-b/a))

isParallel :: (Double,Double)->(Double,Double)->(Double,Double)->(Double,Double)->Bool
--isParallel (1,1) (3,3) (2,0) (4,2)
isParallel (a, b) (c, d) (e, f) (g, h) = if ((c-a)/(d-b)) == ((g-e)/(h-f)) then True else False

isIncluded :: (Double,Double) -> Double -> (Double,Double) -> Double -> Bool
--(x,y,r)
--isIncluded (1,2) 9.3 (4,5) 5.0
--left ассоативная по порядку 6
infixl 6 *+*
a *+* b = (a**2)+(b**2)

isIncluded (x1,y1) r1 (x2,y2) r2 = if r1<(r2+sqrt(abs(x2-x1)*+*abs(y2-y1))) then True else False

isRectangular :: (Double,Double) -> (Double,Double) -> (Double,Double) -> Bool
--isRectangular (0,0) (2,0) (2,2)
isRectangular (x1,y1) (x2,y2) (x3,y3) = if (x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)==0 || (x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)==0 || (x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)==0 then True else False

isTriangle :: Double -> Double -> Double-> Bool
--
isTriangle a b c = if (((a+b)>c && (a-b)<c) || ((a+c)>b && (a-c)<b) || ((c+b)>a && (c-b)<a)) then True else False
--max3

isSorted :: Double -> Double -> Double -> Bool

isSorted a b c = if (a<b && b<c) || (a>b && b>c) then True else False
