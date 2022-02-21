from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import datetime

'''

LOGIN

'''
# this section is for login in, previously setting the username and password as it's shown below
user = 'emtech'
password = 'lifestore'
tries = 0 # you only get three chances to get it correctly
validation = False # indicates when both the username and password are correct

while validation == False: 
    if tries == 3: # after three mistakes the program stops running
        exit()
    if input('Username: ') == user and input('Password: ') == password:
        validation = True
        print('Bienvenido, Emtech! :)')
    else:
        tries += 1
        print(f'Datos erroneos, le quedan {3 - tries} intentos')


'''

5 CON MAYORES VENTAS

'''
#sales list contains the id_sale and id_product from all of the sales that were not returned
sales = []
for sale_info in lifestore_sales:
    if sale_info[4] == 0: # no refund
        sales.append(sale_info[0:2]) 

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(sales)):
    if sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1], reverse=True) # the sales_counter list is sorted. getting the most selled items in top

sales_total = [] # this list is going to be used to calculate de total amount of sales
sales_total = sales_counter

print("\nLos 5 artículos con más ventas en general son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

sales_counter.sort(key = lambda x: x[1])
print("\nLos 5 artículos con menos ventas en general son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

'''

10 CON MAS BUSQUEDAS

'''

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = lifestore_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(lifestore_searches)):
    if lifestore_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [lifestore_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = lifestore_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [lifestore_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the most searched items in top

print("\nLos 10 artículos con más busquedas en general son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break


'''

POR CATEGORIA

PROCESADORES

'''
# the list procesadores contains all of the products from the procesadores category
# procesadores_sales contains the sales of items from procesadores category
# procesadores_searches contains the searches made from items of such category
procesadores = []
procesadores_sales = []
procesadores_searches = []
for product in lifestore_products:
    if product[3] == 'procesadores': # 'procesadores' category
        procesadores.append(product[0:2])
for item in procesadores:
    for sale in sales:
        if item[0] == sale[1]:
            procesadores_sales.append(sale[0:2]) # saves id_sale and id_product for sales of processors only
    for search in lifestore_searches:
        if item[0] == search[1]: # saves search info of processors items
            procesadores_searches.append(search)


# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = procesadores_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(procesadores_sales)):
    if procesadores_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [procesadores_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = procesadores_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [procesadores_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría procesadores son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break


# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = procesadores_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(procesadores_searches)):
    if procesadores_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [procesadores_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = procesadores_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [procesadores_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria procesadores son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

TARJETAS DE VIDEO

'''

tarjetas_de_video = []
tarjetas_de_video_sales = []
tarjetas_de_video_searches = []
for product in lifestore_products:
    if product[3] == 'tarjetas de video': # 'tarjetas de video' category
        tarjetas_de_video.append(product[0:2]) 
for item in tarjetas_de_video:
    for sale in sales:
        if item[0] == sale[1]:
          tarjetas_de_video_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only
    for search in lifestore_searches:
        if item[0] == search[1]:
            tarjetas_de_video_searches.append(search)

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = tarjetas_de_video_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(tarjetas_de_video_sales)):
    if tarjetas_de_video_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [tarjetas_de_video_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = tarjetas_de_video_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [tarjetas_de_video_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría tarjetas de video son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = tarjetas_de_video_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(tarjetas_de_video_searches)):
    if tarjetas_de_video_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [tarjetas_de_video_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = tarjetas_de_video_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [tarjetas_de_video_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria tarjetas de video son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

TARJETAS MADRE

'''

tarjetas_madre = []
tarjetas_madre_sales = []
tarjetas_madre_searches = []
for product in lifestore_products:
    if product[3] == 'tarjetas madre': # 'tarjetas madre' category
        tarjetas_madre.append(product[0:2]) 
for item in tarjetas_madre:
    for sale in sales:
        if item[0] == sale[1]:
          tarjetas_madre_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only
    for search in lifestore_searches:
        if item[0] == search[1]:
            tarjetas_madre_searches.append(search)

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = tarjetas_madre_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(tarjetas_madre_sales)):
    if tarjetas_madre_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [tarjetas_madre_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = tarjetas_madre_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [tarjetas_madre_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría tarjetas madre son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = tarjetas_madre_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(tarjetas_madre_searches)):
    if tarjetas_madre_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [tarjetas_madre_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = tarjetas_madre_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [tarjetas_madre_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria tarjetas madre son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

DISCOS DUROS

'''

discos_duros = []
discos_duros_sales = []
discos_duros_searches = []
for product in lifestore_products:
    if product[3] == 'discos duros': # 'discos duros' category
        discos_duros.append(product[0:2])
for item in discos_duros:
    for sale in sales:
        if item[0] == sale[1]:
          discos_duros_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only
    for search in lifestore_searches:
        if item[0] == search[1]:
            discos_duros_searches.append(search)

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = discos_duros_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(discos_duros_sales)):
    if discos_duros_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [discos_duros_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = discos_duros_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [discos_duros_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría discos duros son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = discos_duros_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(discos_duros_searches)):
    if discos_duros_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [discos_duros_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = discos_duros_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [discos_duros_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria discos duros son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

MEMORIAS USB

'''

memorias_usb = []
memorias_usb_sales = []
for product in lifestore_products:
    if product[3] == 'memorias usb': # 'memorias usb' category
        memorias_usb.append(product[0:2])
for item in memorias_usb:
    for sale in sales:
        if item[0] == sale[1]:
          memorias_usb_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = memorias_usb_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(memorias_usb_sales)):
    if memorias_usb_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [memorias_usb_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = memorias_usb_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [memorias_usb_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría memorias usb son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

print("\nLos 10 artículos con menos busquedas en la categoria memorias usb son:")
print("No se han buscado articulos de la categoria memorias usb.")

'''

PANTALLAS

'''

pantallas = []
pantallas_sales = []
pantallas_searches = []
for product in lifestore_products:
    if product[3] == 'pantallas': # 'pantallas' category
        pantallas.append(product[0:2])
for item in pantallas:
    for sale in sales:
        if item[0] == sale[1]:
          pantallas_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only
    for search in lifestore_searches:
        if item[0] == search[1]:
            pantallas_searches.append(search)

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = pantallas_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(pantallas_sales)):
    if pantallas_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [pantallas_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = pantallas_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [pantallas_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría pantallas son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = pantallas_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(pantallas_searches)):
    if pantallas_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [pantallas_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = pantallas_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [pantallas_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria pantallas son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

BOCINAS

'''

bocinas = []
bocinas_sales = []
bocinas_searches = []
for product in lifestore_products:
    if product[3] == 'bocinas': # 'bocinas' category
        bocinas.append(product[0:2])
for item in bocinas:
    for sale in sales:
        if item[0] == sale[1]:
          bocinas_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only
    for search in lifestore_searches:
        if item[0] == search[1]:
            bocinas_searches.append(search)

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = bocinas_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(bocinas_sales)):
    if bocinas_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [bocinas_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = bocinas_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [bocinas_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría bocinas son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = bocinas_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(bocinas_searches)):
    if bocinas_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [bocinas_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = bocinas_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [bocinas_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria bocinas son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

AUDIFONOS

'''

audifonos = []
audifonos_sales = []
audifonos_searches = []
for product in lifestore_products:
    if product[3] == 'audifonos': # 'audifonos' category
        audifonos.append(product[0:2])
for item in audifonos:
    for sale in sales:
        if item[0] == sale[1]:
          audifonos_sales.append(sale[0:2]) # saves id_sale and id_product for sales of graphic cards only
    for search in lifestore_searches:
        if item[0] == search[1]:
            audifonos_searches.append(search)

# in this section a list sales_counter is created to compute the total sales for each product
previous_idproduct = audifonos_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
sales_counter = [] # sales_counter saves the information of how many times an item was sold
current_article_sales_counter = 0 # variable that counts the individual sale of each product to add it to the sales_counter list
for i in range(len(audifonos_sales)):
    if audifonos_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        current_article_sales_counter += 1
    else:
        temp = [audifonos_sales[i-1][1], current_article_sales_counter] # in this temporary list the id_product and its total sales are saved
        sales_counter.append(temp) # the temp list is added to sales_counter, getting the final results there
        current_article_sales_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = audifonos_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [audifonos_sales[i-1][1], current_article_sales_counter]
sales_counter.append(temp)
sales_counter.sort(key = lambda x: x[1]) # the sales_counter list is sorted. getting the least selled items in top

print("\nLos 5 artículos con menos ventas en la categoría audifonos son:")
counter = 0 # it counts just to 5 printings
for sale in sales_counter:
    for product in lifestore_products:
        if product[0] == sale[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de ventas: {sale[1]}')
            counter += 1
    if counter == 5:
        break

# in this section a list searches_counter is created to compute the total searches for each product
previous_idproduct = audifonos_searches[0][1] # this variable contains the id_product from the previous product to compare it with the current one
searches_counter = [] # searches_counter saves the information of how many times an item was searched
current_article_searches_counter = 0 # variable that counts the individual search of each product to add it to the searches_counter list
for i in range(len(audifonos_searches)):
    if audifonos_searches[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for searches 
        current_article_searches_counter += 1
    else:
        temp = [audifonos_searches[i-1][1], current_article_searches_counter] # in this temporary list the id_product and its total of searches are saved
        searches_counter.append(temp) # the temp list is added to searches_counter, getting the final results there
        current_article_searches_counter = 1 # a new product is being analyzed, so the counter resets to 1
    previous_idproduct = audifonos_searches[i][1] # now the actual id_product is the previous one for the next iteration

temp = [audifonos_searches[i-1][1], current_article_searches_counter]
searches_counter.append(temp)
searches_counter.sort(key = lambda x: x[1], reverse=True) # the searches_counter list is sorted. getting the least searched items in top

print("\nLos 10 artículos con menos busquedas en la categoria audifonos son:")
counter = 0 # it counts just to 10 printings
for search in searches_counter:
    for product in lifestore_products:
        if product[0] == search[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Total de búsquedas: {search[1]}')
            counter += 1
    if counter == 10:
        break

'''

POR RESEÑA

'''

# in this section a list reviews is created to compute the score average of reviews for each product
previous_idproduct = lifestore_sales[0][1] # this variable contains the id_product from the previous product to compare it with the current one
review_sum = 0 # sums the reviews score for each product being analyzed
product_reviews_counter = 0 # counts how many reviews of each product analyzed are
reviews_average = 0 #makes an average of the scores for each product
reviews = [] # reviews saves the average score for each product
for i in range(len(lifestore_sales)):
    if lifestore_sales[i][1] == previous_idproduct: # if the actual id_product is equal to the previous one, increase the counter for sales 
        product_reviews_counter += 1
        review_sum = review_sum + lifestore_sales[i][2]
    else:
        reviews_average = review_sum/product_reviews_counter
        temp = [lifestore_sales[i-1][1], reviews_average] # in this temporary list the id_product and its total sales are saved
        reviews.append(temp) # the temp list is added to sales_counter, getting the final results there
        product_reviews_counter = 1 # a new product is being analyzed, so the counter resets to 1
        review_sum = lifestore_sales[i][2]
    previous_idproduct = lifestore_sales[i][1] # now the actual id_product is the previous one for the next iteration

temp = [lifestore_sales[i-1][1], reviews_average]
reviews.append(temp)
reviews.sort(key = lambda x: x[1], reverse=True) # the sales_counter list is sorted. getting the best rated items in top

print("\nLos 5 artículos con mejores reseñas son:")
counter = 0 # it counts just to 5 printings
for review in reviews:
    for product in lifestore_products:
        if product[0] == review[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Puntaje promedio: {review[1]}')
            counter += 1
    if counter == 5:
        break

reviews.sort(key = lambda x: x[1]) # the sales_counter list is sorted again. getting the worst rated items in top

print("\nLos 5 artículos con peores reseñas son:")
counter = 0 # it counts just to 5 printings
for review in reviews:
    for product in lifestore_products:
        if product[0] == review[0]: #if the id_product on both lists matches, then print the name of the product
            print(f'ID: {product[0]}, Nombre: {product[1]}, Puntaje promedio: {review[1]}')
            counter += 1
    if counter == 5:
        break

'''

TOTAL DE INGRESOS

'''
total_income_product = 0 # this vriable sums the total income from the database
for price in lifestore_products:
    for sale in sales_total:
        if sale[0] == price[0]: # id_product
            total_income_product = total_income_product + sale[1]*price[2] # each iteration sums the multiplication of the amount of sales by the price of the product
print(f'\nEl total de ingresos es de: {total_income_product}\n')

'''

VENTAS POR MES

'''
sales_dates = []
for sale in lifestore_sales:
    if sale[4] == 0: # not a refund
        dates = [sale[1], sale[3][3:5]]
        sales_dates.append(dates)

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
sales_per_month = [0,0,0,0,0,0,0,0,0,0,0,0]
for date in sales_dates:
    for sale in lifestore_products:
        if date[1] == '01' and date[0] == sale[0]:
            sales_per_month[0] += sale[2]
        if date[1] == '02' and date[0] == sale[0]:
            sales_per_month[1] += sale[2]
        if date[1] == '03' and date[0] == sale[0]:
            sales_per_month[2] += sale[2]
        if date[1] == '04' and date[0] == sale[0]:
            sales_per_month[3] += sale[2]
        if date[1] == '05' and date[0] == sale[0]:
            sales_per_month[4] += sale[2]
        if date[1] == '06' and date[0] == sale[0]:
            sales_per_month[5] += sale[2]
        if date[1] == '07' and date[0] == sale[0]:
            sales_per_month[6] += sale[2]
        if date[1] == '08' and date[0] == sale[0]:
            sales_per_month[7] += sale[2]
        if date[1] == '09' and date[0] == sale[0]:
            sales_per_month[8] += sale[2]
        if date[1] == '10' and date[0] == sale[0]:
            sales_per_month[9] += sale[2]
        if date[1] == '11' and date[0] == sale[0]:
            sales_per_month[10] += sale[2]
        if date[1] == '12' and date[0] == sale[0]:
            sales_per_month[11] += sale[2]

for i in range(12):
    print(f'El total de ventas en {months[i]} es de: {sales_per_month[i]}')