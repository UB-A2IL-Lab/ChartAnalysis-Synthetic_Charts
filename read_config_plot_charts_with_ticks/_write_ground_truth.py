import json
import cv2

def create_ground_truth_json(plt, ax, fig, filename, directoryName, chart_title, x_label, y_label, i_axis_visible, label_visible):

    #add title
    titlePlt = plt.title(chart_title)
    bbox_title = titlePlt.get_window_extent(fig.canvas.get_renderer());


    data = {}
    print(titlePlt)

    data['TITLE'] = {}
    data['TITLE'] = {
        "TEXT" : chart_title,
        "BB" : {
            'HEIGHT': int(bbox_title.y1),
            'WIDTH': int(bbox_title.x1),
            'X0': int(bbox_title.x0),
            'Y0': int(bbox_title.y0)
        }
    };


    # x_ticks_labels = [tick for tick in plt.gca().get_xticklabels()]
    # y_ticks_labels = [tick for tick in plt.gca().get_yticklabels()]


    data['X_AXIS'] = {}
    data['Y_AXIS'] = {}
    data['X_AXIS'] = {
        'LABEL_BLOCKS' : [],
        'MAJOR_TICK_LABELS' : [],
        'MINOR_TICK_LABELS' : [],
        'TICK_BLOCKS' : [],
        'X_AXIS_LABEL' : {}
    }

    data['Y_AXIS'] = {
        'LABEL_BLOCKS' : [],
        'MAJOR_TICK_LABELS' : [],
        'MINOR_TICK_LABELS' : [],
        'TICK_BLOCKS' : [],
        'Y_AXIS_LABEL' : {},

    }

    xlbl = ax.xaxis.get_label()
    bbox_xlbl = xlbl.get_window_extent(fig.canvas.get_renderer());
    data['X_AXIS']['X_AXIS_LABEL'] = {
        "BB": {
            "HEIGHT": int(bbox_xlbl.y1),
            "WIDTH": int(bbox_xlbl.x1),
            "X0": int(bbox_xlbl.x0),
            "Y0": int(bbox_xlbl.y0)
        },
        "TEXT": x_label
    }

    ylbl = ax.yaxis.get_label()
    bbox_ylbl = ylbl.get_window_extent(fig.canvas.get_renderer());
    data['Y_AXIS']['Y_AXIS_LABEL'] = {
        "BB": {
            "HEIGHT": int(bbox_ylbl.y1),
            "WIDTH": int(bbox_ylbl.x1),
            "X0": int(bbox_ylbl.x0),
            "Y0": int(bbox_ylbl.y0)
        },
        "TEXT": y_label
    }


    x_ticks_labels = [tick for tick in plt.gca().get_xticklabels()]
    y_ticks_labels = [tick for tick in plt.gca().get_yticklabels()]

    if(label_visible=="TRUE"):
        for i, t in enumerate(x_ticks_labels):
            bbox = t.get_window_extent(fig.canvas.get_renderer());
            # if(   i!=(len(x_ticks_labels))):
            print("processing x tick label .... i = ",i);
            data['X_AXIS']['LABEL_BLOCKS'].append({
                "BB": {
                  "HEIGHT": int( bbox.y1),
                  "WIDTH": int(bbox.x1),
                  "X0": int(bbox.x0),
                  "Y0": int(bbox.y0)
                },
                "ID": i,
                "TEXT": t.get_text()+""
            });
    else:
         del data['X_AXIS']['LABEL_BLOCKS'];

    if(label_visible=="TRUE"):
        for i, t in enumerate(y_ticks_labels):
            bbox = t.get_window_extent(fig.canvas.get_renderer());
            print("processing y_ticks_labels .... i = ",i);
            # if(   i!=(len(y_ticks_labels)-1)):
            data['Y_AXIS']['LABEL_BLOCKS'].append({
                "BB": {
                  "HEIGHT": int( bbox.y1),
                  "WIDTH": int(bbox.x1),
                  "X0": int(bbox.x0),
                  "Y0": int(bbox.y0)
                },
                "ID": i,
                "TEXT": t.get_text()+""
            });
    else:
         del data['Y_AXIS']['LABEL_BLOCKS'];

    # #major tick Labels
    # x_major_ticks_labels = [tick for tick in plt.gca().get_xmajorticklabels()]
    # y_major_ticks_labels = [tick for tick in plt.gca().get_ymajorticklabels()]
    #
    #
    # for i, t in enumerate(x_major_ticks_labels):
    #     bbox = t.get_window_extent(fig.canvas.get_renderer());
    #     if( i!=(len(x_major_ticks_labels))):
    #         data['X_AXIS']['MAJOR_TICK_LABELS'].append({
    #             "BB": {
    #               "HEIGHT": int( bbox.y1),
    #               "WIDTH": int(bbox.x1),
    #               "X0": int(bbox.x0),
    #               "Y0": int(bbox.y0)
    #             },
    #             "ID": i,
    #             "TEXT": t.get_text()+""
    #         });
    #
    #
    #
    # for i, t in enumerate(y_major_ticks_labels):
    #     bbox = t.get_window_extent(fig.canvas.get_renderer());
    #     if( i!=(len(y_major_ticks_labels))):
    #         data['Y_AXIS']['MAJOR_TICK_LABELS'].append({
    #             "BB": {
    #               "HEIGHT": int( bbox.y1),
    #               "WIDTH": int(bbox.x1),
    #               "X0": int(bbox.x0),
    #               "Y0": int(bbox.y0)
    #             },
    #             "ID": i,
    #             "TEXT": t.get_text()+""
    #         });

    ##########################################
    ##########################################

    # #MINOR TICK Labels
    #
    # #minor tick Labels
    # x_minor_ticks_labels = [tick for tick in plt.gca().get_xminorticklabels()]
    # y_minor_ticks_labels = [tick for tick in plt.gca().get_yminorticklabels()]
    #
    # print("len of x_minor_ticks_labels = ", len(x_minor_ticks_labels));
    # for i, t in enumerate(x_minor_ticks_labels):
    #     bbox = t.get_window_extent(fig.canvas.get_renderer());
    #     if(  i!=(len(x_minor_ticks_labels))):
    #         print("processing  i = ", i);
    #         data['X_AXIS']['MINOR_TICK_LABELS'].append({
    #             "BB": {
    #               "HEIGHT": int( bbox.y1),
    #               "WIDTH": int(bbox.x1),
    #               "X0": int(bbox.x0),
    #               "Y0": int(bbox.y0)
    #             },
    #             "ID": i,
    #             "TEXT": t.get_text()+""
    #         });
    #
    # print("len of y_minor_ticks_labels = ", len(y_minor_ticks_labels));
    # for i, t in enumerate(y_minor_ticks_labels):
    #     bbox = t.get_window_extent(fig.canvas.get_renderer());
    #     if(  i!=(len(y_minor_ticks_labels))):
    #         data['Y_AXIS']['MINOR_TICK_LABELS'].append({
    #             "BB": {
    #               "HEIGHT": int( bbox.y1),
    #               "WIDTH": int(bbox.x1),
    #               "X0": int(bbox.x0),
    #               "Y0": int(bbox.y0)
    #             },
    #             "ID": i,
    #             "TEXT": t.get_text()+""
    #         });


    ################################################
    ################################################

    # x_ticks = [tick for tick in ax.get_xticks(minor=True)]
    # y_ticks = [tick for tick in ax.get_yticks(minor=True)]

    #//uncomment later
    x_ticks = [tick for tick in ax.get_xticks()]
    y_ticks = [tick for tick in ax.get_yticks()]

    ymin, _ = ax.get_ylim()
    print("len of x_ticks = ", len(x_ticks));
    for i, t in enumerate(x_ticks):
        # if( i!=(len(x_ticks))):
        display_coord_x = ax.transData.transform((t, ymin))
        data['X_AXIS']['TICK_BLOCKS'].append({
            "BB": {
              # "HEIGHT": int( display_coord_x[1]+5),
              # "WIDTH": int(display_coord_x[0]+5),
              # "X0": int(display_coord_x[0]-5),
              # "Y0": int(display_coord_x[1]-5)
              "X": int(display_coord_x[0]),
              "Y": int(display_coord_x[1])
            },
            "ID": i
        });


    xmin, _ = ax.get_xlim()
    for i, t in enumerate(y_ticks):
        # if(  i!=(len(y_ticks)-1)):
        display_coord_y = ax.transData.transform((xmin, t))
        data['Y_AXIS']['TICK_BLOCKS'].append({
            "BB": {
              # "HEIGHT": int(display_coord_y[1]+5),
              # "WIDTH": int(display_coord_y[0]+5),
              # "X0": int(display_coord_y[0]-5),
              # "Y0": int(display_coord_y[1]-5)
               "X": int(display_coord_y[0]),
               "Y": int(display_coord_y[1])
            },
            "ID": i
        });


    #read title
    bbox_title = ax.get_title();
    #draw bbox for entire image
    xmin,xmax = ax.get_xlim()
    ymin,ymax = ax.get_ylim()
    display_coord_bottom_left = ax.transData.transform((xmin, ymin))
    display_coord_top_right = ax.transData.transform((xmax, ymax))

    data["PLOT_BB"] = {
        "HEIGHT":  int(display_coord_top_right[1]),
        "WIDTH": int(display_coord_top_right[0]),
        "X0": int(display_coord_bottom_left[0]),
        "Y0": int(display_coord_bottom_left[1])
    }


    with open(directoryName+'/'+filename+'.json', 'w') as outfile:
        json.dump(data, outfile)
