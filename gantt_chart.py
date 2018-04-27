import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np
from datetime import datetime


tasks = [{'task_name': 'Literature review',
          'task_start': '2017-04-10', 'task_end': '2020-02-28'},
         {'task_name': 'Bench-top SBC chemical tests',
          'task_start': '2017-07-31', 'task_end': '2018-03-16'},
         {'task_name': 'Development of SBC model',
          'task_start': '2017-10-09', 'task_end': '2018-12-14'},
         {'task_name': 'Design image acquisition unit',
          'task_start': '2018-01-08', 'task_end': '2018-06-08'},
         {'task_name': 'Confirmation report',
          'task_start': '2018-02-19', 'task_end': '2018-05-11'},
         {'task_name': 'Pilot-scale SBC trials',
          'task_start': '2018-05-21', 'task_end': '2018-06-08'},
         {'task_name': 'First journal paper preparation',
          'task_start': '2018-06-11', 'task_end': '2018-08-10'},
         {'task_name': 'Effluent slurry image acquisition tests',
          'task_start': '2018-07-16', 'task_end': '2018-08-31'},
         {'task_name': 'Development of image analysis algorithm',
          'task_start': '2018-08-13', 'task_end': '2018-11-16'},
         {'task_name': 'Second journal paper preparation',
          'task_start': '2018-11-19', 'task_end': '2019-01-11'},
         {'task_name': 'Building the soft sensor',
          'task_start': '2018-12-03', 'task_end': '2019-03-15'},
         {'task_name': 'Mid-candidature review',
          'task_start': '2019-03-01', 'task_end': '2019-04-10'},
         {'task_name': 'Sensor & reagent tests in pilot SBC',
          'task_start': '2019-04-15', 'task_end': '2019-10-04'},
         {'task_name': 'Analysing pilot trial results',
          'task_start': '2019-08-05', 'task_end': '2019-11-01'},
         {'task_name': 'Third journal paper preparation',
          'task_start': '2019-10-28', 'task_end': '2019-12-27'},
         {'task_name': 'Thesis review',
          'task_start': '2020-02-10', 'task_end': '2020-03-13'},
         {'task_name': 'Dissertation writing',
          'task_start': '2020-01-06', 'task_end': '2020-04-10'}
         ]


def plot_chart(input_tasks):
    task_name = [i['task_name'] for i in input_tasks]
    start_time = [datetime.strptime(i['task_start'], '%Y-%m-%d') for i in input_tasks]
    end_time = [datetime.strptime(i['task_end'], '%Y-%m-%d') for i in input_tasks]
    start_date = min(start_time)
    end_date = max(end_time)

    # color for plots
    cmap = plt.get_cmap('rainbow')
    c = [cmap(x) for x in np.linspace(0, 1, len(tasks))]

    # plot chart
    fig, ax = plt.subplots(figsize=(14, 9))
    y_ticks = []
    for j in range(len(input_tasks)-1, -1, -1):
        ax.hlines(j, start_time[j], end_time[j],
                  linewidth=25, colors=c[j])
        y_ticks.append(task_name[j]+"\n" +
                       '{} to {}'.format(start_time[j].strftime('%d/%b/%y'), end_time[j].strftime('%d/%b/%y')))
    ax.set_xlim([start_date, end_date])
    ax.set_ylim([-1, len(input_tasks)])
    date_fmt = DateFormatter('%d/%b/%y')
    months = MonthLocator(range(1, 13), bymonthday=10, interval=2)
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(date_fmt)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_yticks(np.arange(len(input_tasks)-1, -1, -1))
    ax.set_yticklabels(y_ticks)
    plt.xticks(rotation=80)
    plt.show()


plot_chart(tasks)

