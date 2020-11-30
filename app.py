from flask import Flask, request, jsonify, render_template, make_response, redirect

app = Flask(__name__)

first_names = ['ishraq', 'amy', 'michael', 'bryant']
last_names = ['khan', 'rosa', 'alford', 'novas']
ages = [10, 15, 20, 25]
averages = [90, 95, 100, 104]
    
data_science_class = [{'id': i, 'first_name': first_names[i], 'last_name': last_names[i], 'age': ages[i], 'average': averages[i]} for i in range(4)]
last_unique_id = 3

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def get_students():
    return render_template('view.html', data=data_science_class)
        
@app.route('/add', methods=['GET','POST'])
def update_students():
    if request.method == 'POST':
        new_student = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age'],
            'average': request.form['average']
        }
        data_science_class.append(new_student)
        return redirect('/view')
    return render_template('add.html')

@app.route('/remove', methods=['GET', 'POST'])
def remove_student():
    if request.method == 'POST':
        for index, student in enumerate(data_science_class):
            if request.form['first_name'].lower() == student['first_name'].lower():
                data_science_class.pop(index)
                return redirect('/view')
        return redirect('/remove')
    return render_template('remove.html')
                
if __name__ == "__main__":
    app.run(debug=True)
    