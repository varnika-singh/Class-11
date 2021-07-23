from numberutils import analyzer

if __name__ == '__main__':
    nu = analyzer.NumberAnalyzer()
    print("{} is even: {}".format(5, nu.is_even(5)))