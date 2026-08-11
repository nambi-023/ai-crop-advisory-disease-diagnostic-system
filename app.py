from flask import Flask, render_template, request
app = Flask(__name__)

DATA = {
 "Tomato": {
  "healthy": ("Healthy Tomato Leaf","No major warning symptom was selected.","Continue balanced watering, good sunlight, and regular field inspection."),
  "spots": ("Tomato Early Blight (Possible)","Dark spots can be associated with early blight.","Remove badly affected leaves, avoid overhead watering, and improve air circulation."),
  "yellow": ("Tomato Leaf Yellowing (Possible)","Yellowing may be related to nutrient or crop stress.","Check soil nutrients and irrigation and inspect for pests.")
 },
 "Potato": {
  "healthy": ("Healthy Potato Leaf","No major warning symptom was selected.","Maintain proper irrigation and monitor the crop regularly."),
  "spots": ("Potato Early Blight (Possible)","Brown or dark leaf spots can indicate a possible fungal problem.","Remove infected plant material and avoid wetting foliage."),
  "yellow": ("Potato Leaf Yellowing (Possible)","Yellowing can result from nutrient, water, or disease stress.","Check soil moisture and nutrients and inspect plants for additional symptoms.")
 },
 "Rice": {
  "healthy": ("Healthy Rice Plant","No major warning symptom was selected.","Maintain appropriate water management and monitor regularly."),
  "spots": ("Rice Leaf Spot / Disease Stress (Possible)","Leaf spots can be associated with several rice diseases.","Monitor affected plants and consult local agricultural guidance."),
  "yellow": ("Rice Nutrient/Stress Warning","Yellowing may indicate nutrient or environmental stress.","Check water management and soil nutrients.")
 }
}

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        crop = request.form.get("crop","Tomato")
        symptom = request.form.get("symptom","healthy")
        image = request.files.get("leaf_image")
        r = DATA.get(crop, DATA["Tomato"]).get(symptom, DATA["Tomato"]["healthy"])
        result = {"title":r[0],"description":r[1],"advice":r[2],
                  "filename": image.filename if image and image.filename else "No image selected"}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
