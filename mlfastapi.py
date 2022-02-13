from distutils.log import debug
from fastapi import FastAPI
import pickle
import uvicorn
app=FastAPI(debug=True)

@app.post('/')
def predict(text:str):
            model=pickle.load(open('language_prediction.pickle','rb'))
            vectorizer=pickle.load(open('countvectorizer.pickle','rb'))
            #vectorize the text
            test = vectorizer.transform([str(text)])
            #var_test=toNumpyArray(test)
            l=model.predict(test.toarray())
            #Check for the prediction probability
            #pred_proba=model.predict_proba(test.toarray())
            #pred_percentage_for_all=dict(zip(model.classes_,pred_proba[0]))
            #output=round(l[0])
            
            return{'The predicted language is: {}'.format(l[0])}
    #return l[0]
    #jsonify({'the language is':l[0]})
    


if __name__=="__main__":
           uvicorn.run(app)