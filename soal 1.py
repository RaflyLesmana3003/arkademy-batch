import json

# function to return bio
def biodata(name, age):

  #data biodata
  data = {
  "name": name,
  "age": age,
  "address": "gadang gang 1/27 malang",
  "hobbies": [
              'self learning',
              'a little bit of gaming',
              'code'
              ],
  "is_married": 0,
  "list_school": {
                  "smp": {
                      "name": "pondok pesantren alhayatul islamiyah",
                      "year_in": 2014,
                      "year_out": 2016,
                      "major": None
                      },
                  "smk": {
                      "name": "smkn 4 malang",
                      "year_in": 2016,
                      "year_out": 2019,
                      "major": None
                      },
                  },
  "skills": [
             { "name": "web developer",
              "level": "advanced"
              },
             { "name": "content creator",
              "level": "beginner"
              },
             { "name": "machine learning",
              "level": "beginner"
              },
             ],
  "interest_in_coding" : 1            
  }

  # diubah dalam bentuk json
  biodata = json.dumps(data)
  return(biodata)

# memanggil function biodata()
biodata("rafly lesmana", 18) 
