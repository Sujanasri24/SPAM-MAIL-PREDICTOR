from flask import Flask, request, render_template, url_for
import joblib

app = Flask(__name__);

spam_model = joblib.load(open('Spam_mail_model.joblib', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    title = 'Spam Mail detection'

    if request.method == 'GET':
        return render_template('index.html', title = 'Spam mail Detection', test=False)

    else:

        try :
            mail = request.form['mail_content']
            mail = [mail]
            
            prediction = spam_model.predict(mail)
            
            # conclusion part
            if prediction[0]==1: #ham
                # ham = True
                return render_template('index.html', title = title, result = True, test = True)
            else :
                return render_template('index.html', title = title, result= False, test = True)
            
        except :
            pass
   
        

# @app.route('/', methods=['POST'])
# def result():
#     title = 'Spam Mail Detection'
          

if __name__ == "__main__":
    app.run(port=5050, debug=True)