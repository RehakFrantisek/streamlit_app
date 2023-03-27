import streamlit
import pandas
from urllib.error import URLError
import requests
import snowflake.connector


streamlit.title('My Parents New Healthy Diner')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avo toas')




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)

# def section
def get_fruityvice_data(this_fruit_choice):
  fruity_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruity_response.json())


# section to display api response
streamlit.header('Fruityvice Fruit Advice!')

# snowflake function
def get_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM fruit_load_list")
    return my_cur.fetchall()
  
if streamlit.button('Get load'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_list()
  streamlit.dataframe(my_data_rows)
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Select fruit")
  else:
    function_value = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(function_value)
except URLError as e:
  streamlit.error()  
  
  
fruity_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

streamlit.text(fruity_response.json())

# write your own comment -what does the next line do? 


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list containts")
streamlit.text("Hello from Snowflake:")
streamlit.dataframe(my_data_rows)
streamlit.header('What fruit would you like to add?')
fruit_choice2 = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice2:
    streamlit.error("Select fruit")
  else:
    function_value = get_fruityvice_data(fruit_choice2)
    streamlit.dataframe(function_value)

streamlit.stop()


