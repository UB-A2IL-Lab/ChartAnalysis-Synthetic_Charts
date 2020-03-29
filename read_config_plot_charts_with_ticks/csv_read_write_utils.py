import csv
import os.path



def read_csv(fileName):
    with open(fileName) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        line_count = 0
        data = []
        result = {};
        for row in csv_reader:
            if line_count == 0:
                graph_title = row[0]
                result['graph_title'] = graph_title;
                line_count += 1
            elif line_count == 1:
                i_axis_title = row[0]
                # i_axis_labels = row[1:]
                result['i_axis_title'] = i_axis_title;
                # result['i_axis_labels'] = i_axis_labels;
                line_count += 1
            elif line_count == 2:
                d_axis_title = row[0]
                result['d_axis_title'] = d_axis_title;
                d_axis_labels = row[1:]
                result['d_axis_labels'] = d_axis_labels;
                line_count += 1
            elif line_count == 3:
                i_label = row[0]
                d_label = row[1:]
                result['i_label'] = i_label;
                result['d_label'] = d_label;
                line_count += 1
            else:
                data.append(row)
                line_count += 1

        i_data = [];
        d_data = [];

        for j,dt in enumerate(data):
            # print("j = ",j);

            for i,val in enumerate(dt):
                # print(i,",",val)
                if(i>=1):
                    # print(j-1)
                    d_data.append([])
                if(i==0):
                    i_data.append(val)
                else:
                    d_data[i-1].append(val)
                    # print((i-1)," = ",d_data[i-1])
                    # print('===========')
        result['i_data'] = i_data;
        d_data = (filter(None, d_data))
        result['d_data'] = d_data;

        #as per new format for data file (csv) that was decided
        result['i_axis_labels'] = result['i_data'];

        return result;

def write_csv(fileName, csvData):
    # csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']];
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile);
        writer.writerows(csvData);
    csvFile.close();


def write_csv_horizontally(fileName, csvData):
    # csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']];

    # with open(fileName, 'w') as csvFile:
    #     writer = csv.writer(csvFile);
    #     writer.writerows(csvData);
    # csvFile.close();
    f= open(fileName,"w+");
    length = len(csvData[0]);
    for i in range(1, length ):
        f.write(csvData[0][i] +" : "+ str(csvData[1][i])+"\n");
    f.close();



def write_to_csv_line_by_line(fileName, csvData):
    fileExists = os.path.exists(fileName);
    print(fileName);
    if(fileExists != True):
        #initial content

        columns = ['ChartNum', 'Folder_Name', 'File_Link', 'Chart_Type', 'Orientation', 'Tick_Direction', 'Tick_Length', 'Tick_Width','Tick_X_Axis_Major_Locator', 'Tick_X_Axis_Minor_Locator','Tick_X_Axis_Tick_Style', 'Tick_X_Axis_Color', 'Tick_X_Axis_Font_Name', 'Tick_X_Axis_Font_Size', 'Tick_X_Axis_Rotation', 'Tick_Y_Axis_Major_Locator', 'Tick_Y_Axis_Minor_Locator', 'Tick_Y_Axis_Tick_Style', 'Tick_Y_Axis_Color', 'Tick_Y_Axis_Font_Name', 'Tick_Y_Axis_Font_Size', 'Tick_Y_Axis_Rotation', 'ShowGrid', 'Independent_Axis_Scale', 'Independent_Axis_Labels_Source',   'Dependent_Axis_Scale', 'Dependent_Axis_Labels_Source' ]
        with open(fileName,'w') as f:
            writer=csv.writer(f)
            writer.writerow(columns)

    with open(fileName,'a') as f:
        writer=csv.writer(f)
        writer.writerow(csvData)

def append_to_csv(fileName, csvData):
    fileExists = os.path.exists(fileName);
    print(fileName);
    if(fileExists != True):
        #initial content
        with open(fileName,'w') as f:
            f.write('ctype, independent_variable, dependent_variable, chart_title,  x_label, y_label, font_size, line_style, line_width, x_ticks, y_ticks, bar_width, color_array, orientation, legend, chartNum, i_axis_visible, label_visible, output_folder_name\n') # TRAILING NEWLINE

    with open(fileName,'a') as f:
        writer=csv.writer(f)
        writer.writerow(csvData)
