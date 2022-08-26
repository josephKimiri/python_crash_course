grades = 50

if grades >= 70:
    print("\nCongratulations you have got an A")
elif grades in range(60, 70):
    print("\n Well Done you scored a B in your test.")
elif grades in range(50, 60):
    print("\nGreat you have a C in your test")
elif grades in range(40, 50):
    print("\nPass you have a D in the test, Work harder to avoid supplementaries.")
else:
    print("\nSorry! you have a supplementary in your exams.")               