import webbrowser

from flask import Flask, render_template
import Login, time, import_packages
import Fraud_Check, embargo_check, camt_054, flask,Transaction,Dashboard_check,url

app = Flask(__name__)


class TestAppResult:
    def __init__(self):
        self.result_list = []

    def test_app(self):
        url_result = url.check_url()
        login_result = Login.login()
        Fraud_check_result_new = Fraud_Check.fraud_check_fun()
        embargo_check_result_new = embargo_check.embargo_check()
        time.sleep(5)
        camt_54 = camt_054.camt_054()
        time.sleep(4)
        transaction_view_result =Transaction.transaction()
        time.sleep(4)
        dashboard_view = Dashboard_check.Dashboard_check_fun()


        time.sleep(6)

        with open('result_list.txt', 'w') as file:
            file.write(str(url_result) + "\n")
            file.write(str(login_result) + "\n")
            file.write(str(Fraud_check_result_new) + "\n")
            file.write(str(embargo_check_result_new) + "\n")
            file.write(str(camt_54) + "\n")
            file.write(str(transaction_view_result) + "\n")
            file.write(str(dashboard_view) + "\n")


        self.result_list.append(url_result)
        self.result_list.append(login_result)
        self.result_list.append(Fraud_check_result_new)
        self.result_list.append(embargo_check_result_new)
        self.result_list.append(camt_54)
        self.result_list.append(transaction_view_result)
        self.result_list.append(dashboard_view)
        print(self.result_list)

        return url_result,login_result,Fraud_check_result_new, embargo_check_result_new,camt_54,transaction_view_result,dashboard_view


@app.route('/result')
def show_result():
    obj = TestAppResult()
    obj.test_app()
    if len(obj.result_list) >= 2:
      url_result =obj.result_list[0]
      login_result =obj.result_list[1]
      fraud_result = obj.result_list[2]
      embargo_result_new = obj.result_list[3]
      camt_054 = obj.result_list[4]
      transaction_view_result = obj.result_list[5]
      dashboard_view = obj.result_list[6]
      return render_template('Result.html',url_result = url_result,login_result = login_result, fraud_result=fraud_result, embargo_result=embargo_result_new,camt_54_result=camt_054,
                             transaction_view_result = transaction_view_result ,dashboard_view= dashboard_view )
    else:
    # Handle the case where result_list does not have enough elements
      return "Error: Not enough elements in result_list"

if __name__ == '__main__':
    obj = TestAppResult()
    obj.test_app()
    webbrowser.open(url='http://127.0.0.1:4003/result')
    #webbrowser.Chrome.open(url='http://127.0.0.1:4003/result')
    app.run(host='127.0.0.1',port=4003)
    #webbrowser.Chrome.open(url='http://127.0.0.1:4003/result')
