price=int(input("請輸入金額(1~1000):"))
refund=1000-price

n_500=int(refund/500)
refund%=500

n_100=int(refund/100)
refund%=100

n_50=int(refund/50)
refund%=50

n_10=int(refund/10)
refund%=10

n_5=int(refund/5)
refund%=5

n_1=int(refund/1)
refund%=1

print(n_500,"* 500 +",n_100,"* 100 +",n_50,"* 50 +",n_10,"* 10 +",n_5,"* 5 +",n_1,"* 1")