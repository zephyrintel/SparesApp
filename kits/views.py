from django.shortcuts import render
from django.db import connection
from .models import Kit

def kit_selector(request):
    # Clean the selected kit input
    selected_kit_id = request.GET.get('kit', '')

    # Fetch kits from the database
    kits = Kit.objects.all()

    # Initialize variables
    level1_components = []
    level2_components_dict = {}  # Ensure this is a dictionary
    selected_kit_name = None

    if selected_kit_id:
        # Fetch the Kit instance by ID
        kit_instance = Kit.objects.filter(kit_id=selected_kit_id).first()

        if kit_instance:
            # Set the selected kit name
            selected_kit_name = kit_instance.kit_name

            # Define the raw SQL query
            sql_query = """
                SELECT DISTINCT
                    l1.ItemNumber AS Level1_ItemNumber,
                    l1.Description AS Level1_Description,
                    l2.ItemNumber AS Level2_ItemNumber,
                    l2.Description AS Level2_Description,
                    l1.Quantity AS Level1_Quantity,
                    l2.Quantity AS Level2_Quantity
                FROM 
                    Kits k
                JOIN 
                    KitParts kp ON k.KitID = kp.KitID
                JOIN 
                    Level1Components l1 ON kp.PartID = l1.PartID
                LEFT JOIN 
                    Level2Components l2 ON l2.ParentPartID = l1.PartID
                WHERE 
                    k.KitID = %s
                ORDER BY 
                    l1.ItemNumber, l2.ItemNumber;
            """

            # Execute the raw SQL query and fetch results
            with connection.cursor() as cursor:
                cursor.execute(sql_query, [kit_instance.kit_id])
                rows = cursor.fetchall()

            # Parse the results into separate level1 and level2 components
            for row in rows:
                # Append Level 1 components only if they are unique
                if row[0] not in [component['item_number'] for component in level1_components]:
                    level1_components.append({
                        'item_number': row[0],
                        'description': row[1],
                        'quantity': row[4]
                    })

                # Append Level 2 components if they exist and group them under their parent Level 1 component
                if row[2]:  # If Level 2 ItemNumber is not null
                    if row[0] not in level2_components_dict:
                        level2_components_dict[row[0]] = []  # Initialize the list if it doesn't exist
                    level2_components_dict[row[0]].append({
                        'item_number': row[2],
                        'description': row[3],
                        'quantity': row[5]
                    })

    context = {
        'kits': kits,
        'selected_kit_name': selected_kit_name,
        'level1_components': level1_components,
        'level2_components_dict': level2_components_dict,  # Pass the dictionary to the template
    }

    return render(request, 'kits/kit_selector.html', context)
