from flask import Flask, request, jsonify, render_template, make_response

app = Flask(__name__)

first_names = ['ishraq', 'amy', 'michael', 'bryant']
last_names = ['khan', 'rosa', 'alford', 'novas']
ages = [10, 15, 20, 25]
averages = [90, 95, 100, 104]
    
data_science_class = [{'first_name': first_names[i].title(), 'last_name': last_names[i].title(), 'age': ages[i], 'average': averages[i]} for i in range(4)]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def get_students():
    return render_template('view.html', data=data_science_class)
    # response = make_response(
    #     jsonify(data_science_class),
    #     401,
    # )
    # response.headers['Content-Type'] = 'application/json'
    # return response
        
@app.route('/add', methods=['POST'])
def update_students():
    if 

@app.route('/remove')
def remove_student():
    pass



if __name__ == "__main__":
    app.run(debug=True)
    