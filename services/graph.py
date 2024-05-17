import plotly.graph_objects as go

# dynasties = ['Ming', 'Qing', 'Song', 'Tang']
# word_counts = [6195921, 6018716, 6147901, 2063294]
# unique_word_counts = [7729, 8116, 8275, 8225]

dynasties = ['Tang', 'Song', 'Ming', 'Qing']
word_counts = [2063294, 6147901, 6195921, 6018716]
unique_word_counts = [8225, 8275, 7729, 8116]
colors = ['#EF553B', '#636EFA', '#00CC96', '#AB63FA']

def make_graph(counts):
    fig = go.Figure(data = [go.Bar(x=dynasties, y=counts, marker=dict(color=colors))])

    fig.update_layout(
        xaxis_title='Dynasty',
        yaxis_title=f'Instance Count'
    )

    return fig

def make_unique_graph(counts):
    counts = [counts[i] / unique_word_counts[i] for i in range(len(counts))]

    fig = go.Figure(data = [go.Bar(x=dynasties, y=counts, marker=dict(color=colors))])

    fig.update_layout(
        xaxis_title='Dynasty',
        yaxis_title=f'Instance Count / Unique Character Count'
    )

    return fig

def make_total_graph(counts):
    counts = [counts[i] / word_counts[i] for i in range(len(counts))]

    fig = go.Figure(data = [go.Bar(x=dynasties, y=counts, marker=dict(color=colors))])

    fig.update_layout(
        xaxis_title='Dynasty',
        yaxis_title=f'Instance Count / Total Character Count'
    )

    return fig

def get_total_characters_graph():
    fig = go.Figure(data = [go.Pie(labels=dynasties, values=word_counts, textinfo='label+value')])

    fig.update_layout(
        title='Total Character Counts by Dynasty'
    )

    return fig

def get_unique_characters_graph():
    fig = go.Figure(data = [go.Pie(labels=dynasties, values=unique_word_counts,textinfo='label+value')])

    fig.update_layout(
        title='Unique Character Counts by Dynasty'
    )

    return fig