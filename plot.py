import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go

def Double_Exponential_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Double_Exponential_Moving_Average'],name='Double Exponential Moving Average'))
    fig1.update_layout(title='Double Exponential Moving Average',xaxis_title='Time',yaxis_title='Double Exponential Moving Average')
    return fig1
def Exponential_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Exponential_Moving_Average'],name='Exponential Moving Average'))
    fig1.update_layout(title='Exponential Moving Average',xaxis_title='Time',yaxis_title='Exponential Moving Average')
    return fig1
def Hilbert_Transform___Instantaneous_Trendline_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Hilbert_Transform___Instantaneous_Trendline'],name='Hilbert Transform - Instantaneous Trendline'))
    fig1.update_layout(title='Hilbert Transform - Instantaneous Trendline',xaxis_title='Time',yaxis_title='Hilbert Transform - Instantaneous Trendline')
    return fig1
def Kaufman_Adaptive_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Kaufman_Adaptive_Moving_Average'],name='Kaufman Adaptive Moving Average'))
    fig1.update_layout(title='Kaufman Adaptive Moving Average',xaxis_title='Time',yaxis_title='Kaufman Adaptive Moving Average')
    return fig1
def Moving_average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_average'],name='Moving average'))
    fig1.update_layout(title='Moving average',xaxis_title='Time',yaxis_title='Moving average')
    return fig1
def Moving_average_with_variable_period_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_average_with_variable_period'],name='Moving average with variable period'))
    fig1.update_layout(title='Moving average with variable period',xaxis_title='Time',yaxis_title='Moving average with variable period')
    return fig1
def MidPoint_over_period_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['MidPoint_over_period'],name='MidPoint over period'))
    fig1.update_layout(title='MidPoint over period',xaxis_title='Time',yaxis_title='MidPoint over period')
    return fig1
def Midpoint_Price_over_period_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Midpoint_Price_over_period'],name='Midpoint Price over period'))
    fig1.update_layout(title='Midpoint Price over period',xaxis_title='Time',yaxis_title='Midpoint Price over period')
    return fig1
def Parabolic_SAR_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Parabolic_SAR'],name='Parabolic SAR'))
    fig1.update_layout(title='Parabolic SAR',xaxis_title='Time',yaxis_title='Parabolic SAR')
    return fig1
def Parabolic_SAR___Extended_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Parabolic_SAR___Extended'],name='Parabolic SAR - Extended'))
    fig1.update_layout(title='Parabolic SAR - Extended',xaxis_title='Time',yaxis_title='Parabolic SAR - Extended')
    return fig1
def Simple_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Simple_Moving_Average'],name='Simple Moving Average'))
    fig1.update_layout(title='Simple Moving Average',xaxis_title='Time',yaxis_title='Simple Moving Average')
    return fig1
def Triple_Exponential_Moving_Average_T3_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Triple_Exponential_Moving_Average_T3'],name='Triple Exponential Moving Average (T3)'))
    fig1.update_layout(title='Triple Exponential Moving Average (T3)',xaxis_title='Time',yaxis_title='Triple Exponential Moving Average (T3)')
    return fig1
def Triple_Exponential_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Triple_Exponential_Moving_Average'],name='Triple Exponential Moving Average'))
    fig1.update_layout(title='Triple Exponential Moving Average',xaxis_title='Time',yaxis_title='Triple Exponential Moving Average')
    return fig1
def Triangular_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Triangular_Moving_Average'],name='Triangular Moving Average'))
    fig1.update_layout(title='Triangular Moving Average',xaxis_title='Time',yaxis_title='Triangular Moving Average')
    return fig1
def Weighted_Moving_Average_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Weighted_Moving_Average'],name='Weighted Moving Average'))
    fig1.update_layout(title='Weighted Moving Average',xaxis_title='Time',yaxis_title='Weighted Moving Average')
    return fig1
def Average_Directional_Movement_Index_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Average_Directional_Movement_Index'],name='Average Directional Movement Index'))
    fig1.update_layout(title='Average Directional Movement Index',xaxis_title='Time',yaxis_title='Average Directional Movement Index')
    return fig1
def Average_Directional_Movement_Index_Rating_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Average_Directional_Movement_Index_Rating'],name='Average Directional Movement Index Rating'))
    fig1.update_layout(title='Average Directional Movement Index Rating',xaxis_title='Time',yaxis_title='Average Directional Movement Index Rating')
    return fig1
def Absolute_Price_Oscillator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Absolute_Price_Oscillator'],name='Absolute Price Oscillator'))
    fig1.update_layout(title='Absolute Price Oscillator',xaxis_title='Time',yaxis_title='Absolute Price Oscillator')
    return fig1
def Aroon_Oscillator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Aroon_Oscillator'],name='Aroon Oscillator'))
    fig1.update_layout(title='Aroon Oscillator',xaxis_title='Time',yaxis_title='Aroon Oscillator')
    return fig1
def Balance_Of_Power_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Balance_Of_Power'],name='Balance Of Power'))
    fig1.update_layout(title='Balance Of Power',xaxis_title='Time',yaxis_title='Balance Of Power')
    return fig1
def Commodity_Channel_Index_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Commodity_Channel_Index'],name='Commodity Channel Index'))
    fig1.update_layout(title='Commodity Channel Index',xaxis_title='Time',yaxis_title='Commodity Channel Index')
    return fig1
def Chande_Momentum_Oscillator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Chande_Momentum_Oscillator'],name='Chande Momentum Oscillator'))
    fig1.update_layout(title='Chande Momentum Oscillator',xaxis_title='Time',yaxis_title='Chande Momentum Oscillator')
    return fig1
def Directional_Movement_Index_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Directional_Movement_Index'],name='Directional Movement Index'))
    fig1.update_layout(title='Directional Movement Index',xaxis_title='Time',yaxis_title='Directional Movement Index')
    return fig1
def MACD_with_controllable_MA_type_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['MACD_with_controllable_MA_type'],name='MACD with controllable MA type'))
    fig1.update_layout(title='MACD with controllable MA type',xaxis_title='Time',yaxis_title='MACD with controllable MA type')
    return fig1
def Money_Flow_Index_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Money_Flow_Index'],name='Money Flow Index'))
    fig1.update_layout(title='Money Flow Index',xaxis_title='Time',yaxis_title='Money Flow Index')
    return fig1
def Minus_Directional_Indicator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Minus_Directional_Indicator'],name='Minus Directional Indicator'))
    fig1.update_layout(title='Minus Directional Indicator',xaxis_title='Time',yaxis_title='Minus Directional Indicator')
    return fig1
def Minus_Directional_Movement_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Minus_Directional_Movement'],name='Minus Directional Movement'))
    fig1.update_layout(title='Minus Directional Movement',xaxis_title='Time',yaxis_title='Minus Directional Movement')
    return fig1
def Momentum_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Momentum'],name='Momentum'))
    fig1.update_layout(title='Momentum',xaxis_title='Time',yaxis_title='Momentum')
    return fig1
def Plus_Directional_Indicator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Plus_Directional_Indicator'],name='Plus Directional Indicator'))
    fig1.update_layout(title='Plus Directional Indicator',xaxis_title='Time',yaxis_title='Plus Directional Indicator')
    return fig1
def Plus_Directional_Movement_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Plus_Directional_Movement'],name='Plus Directional Movement'))
    fig1.update_layout(title='Plus Directional Movement',xaxis_title='Time',yaxis_title='Plus Directional Movement')
    return fig1
def Percentage_Price_Oscillator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Percentage_Price_Oscillator'],name='Percentage Price Oscillator'))
    fig1.update_layout(title='Percentage Price Oscillator',xaxis_title='Time',yaxis_title='Percentage Price Oscillator')
    return fig1
def Rate_of_change_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Rate_of_change'],name='Rate of change'))
    fig1.update_layout(title='Rate of change',xaxis_title='Time',yaxis_title='Rate of change')
    return fig1
def Rate_of_change_Percentage_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Rate_of_change_Percentage'],name='Rate of change Percentage'))
    fig1.update_layout(title='Rate of change Percentage',xaxis_title='Time',yaxis_title='Rate of change Percentage')
    return fig1
def Rate_of_change_ratio_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Rate_of_change_ratio'],name='Rate of change ratio'))
    fig1.update_layout(title='Rate of change ratio',xaxis_title='Time',yaxis_title='Rate of change ratio')
    return fig1
def Rate_of_change_ratio_100_scale_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Rate_of_change_ratio_100_scale'],name='Rate of change ratio 100 scale'))
    fig1.update_layout(title='Rate of change ratio 100 scale',xaxis_title='Time',yaxis_title='Rate of change ratio 100 scale')
    return fig1
def Relative_Strength_Index_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Relative_Strength_Index'],name='Relative Strength Index'))
    fig1.update_layout(title='Relative Strength Index',xaxis_title='Time',yaxis_title='Relative Strength Index')
    return fig1
def one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA'],name='one-day Rate-Of-Change ROC of a Triple Smooth EMA'))
    fig1.update_layout(title='one-day Rate-Of-Change ROC of a Triple Smooth EMA',xaxis_title='Time',yaxis_title='one-day Rate-Of-Change ROC of a Triple Smooth EMA')
    return fig1
def Ultimate_Oscillator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Ultimate_Oscillator'],name='Ultimate Oscillator'))
    fig1.update_layout(title='Ultimate Oscillator',xaxis_title='Time',yaxis_title='Ultimate Oscillator')
    return fig1
def Williams_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Williams'],name='Williams'))
    fig1.update_layout(title='Williams',xaxis_title='Time',yaxis_title='Williams')
    return fig1
def Chaikin_AD_Line_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Chaikin_AD_Line'],name='Chaikin A/D Line'))
    fig1.update_layout(title='Chaikin A/D Line',xaxis_title='Time',yaxis_title='Chaikin A/D Line')
    return fig1
def Chaikin_AD_Oscillator_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Chaikin_AD_Oscillator'],name='Chaikin A/D Oscillator'))
    fig1.update_layout(title='Chaikin A/D Oscillator',xaxis_title='Time',yaxis_title='Chaikin A/D Oscillator')
    return fig1
def On_Balance_Volume_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['On_Balance_Volume'],name='On Balance Volume'))
    fig1.update_layout(title='On Balance Volume',xaxis_title='Time',yaxis_title='On Balance Volume')
    return fig1
def Two_Crows_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Two_Crows'],name='Two Crows'))
    fig1.update_layout(title='Two Crows',xaxis_title='Time',yaxis_title='Two Crows')
    return fig1
def Three_Black_Crows_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Three_Black_Crows'],name='Three Black Crows'))
    fig1.update_layout(title='Three Black Crows',xaxis_title='Time',yaxis_title='Three Black Crows')
    return fig1
def Three_Inside_UpDown_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Three_Inside_UpDown'],name='Three Inside Up/Down'))
    fig1.update_layout(title='Three Inside Up/Down',xaxis_title='Time',yaxis_title='Three Inside Up/Down')
    return fig1
def Three_Line_Strike_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Three_Line_Strike'],name='Three-Line Strike'))
    fig1.update_layout(title='Three-Line Strike',xaxis_title='Time',yaxis_title='Three-Line Strike')
    return fig1
def Three_Outside_UpDown_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Three_Outside_UpDown'],name='Three Outside Up/Down'))
    fig1.update_layout(title='Three Outside Up/Down',xaxis_title='Time',yaxis_title='Three Outside Up/Down')
    return fig1
def Three_Stars_In_The_South_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Three_Stars_In_The_South'],name='Three Stars In The South'))
    fig1.update_layout(title='Three Stars In The South',xaxis_title='Time',yaxis_title='Three Stars In The South')
    return fig1
def Three_Advancing_White_Soldiers_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Three_Advancing_White_Soldiers'],name='Three Advancing White Soldiers'))
    fig1.update_layout(title='Three Advancing White Soldiers',xaxis_title='Time',yaxis_title='Three Advancing White Soldiers')
    return fig1
def Abandoned_Baby_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Abandoned_Baby'],name='Abandoned Baby'))
    fig1.update_layout(title='Abandoned Baby',xaxis_title='Time',yaxis_title='Abandoned Baby')
    return fig1
def Advance_Block_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Advance_Block'],name='Advance Block'))
    fig1.update_layout(title='Advance Block',xaxis_title='Time',yaxis_title='Advance Block')
    return fig1
def Belt_hold_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Belt_hold'],name='Belt-hold'))
    fig1.update_layout(title='Belt-hold',xaxis_title='Time',yaxis_title='Belt-hold')
    return fig1
def Breakaway_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Breakaway'],name='Breakaway'))
    fig1.update_layout(title='Breakaway',xaxis_title='Time',yaxis_title='Breakaway')
    return fig1
def Closing_Marubozu_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Closing_Marubozu'],name='Closing Marubozu'))
    fig1.update_layout(title='Closing Marubozu',xaxis_title='Time',yaxis_title='Closing Marubozu')
    return fig1
def Concealing_Baby_Swallow_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Concealing_Baby_Swallow'],name='Concealing Baby Swallow'))
    fig1.update_layout(title='Concealing Baby Swallow',xaxis_title='Time',yaxis_title='Concealing Baby Swallow')
    return fig1
def Counterattack_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Counterattack'],name='Counterattack'))
    fig1.update_layout(title='Counterattack',xaxis_title='Time',yaxis_title='Counterattack')
    return fig1
def Dark_Cloud_Cover_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Dark_Cloud_Cover'],name='Dark Cloud Cover'))
    fig1.update_layout(title='Dark Cloud Cover',xaxis_title='Time',yaxis_title='Dark Cloud Cover')
    return fig1
def Doji_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Doji'],name='Doji'))
    fig1.update_layout(title='Doji',xaxis_title='Time',yaxis_title='Doji')
    return fig1
def Doji_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Doji_Star'],name='Doji Star'))
    fig1.update_layout(title='Doji Star',xaxis_title='Time',yaxis_title='Doji Star')
    return fig1
def Dragonfly_Doji_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Dragonfly_Doji'],name='Dragonfly Doji'))
    fig1.update_layout(title='Dragonfly Doji',xaxis_title='Time',yaxis_title='Dragonfly Doji')
    return fig1
def Engulfing_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Engulfing_Pattern'],name='Engulfing Pattern'))
    fig1.update_layout(title='Engulfing Pattern',xaxis_title='Time',yaxis_title='Engulfing Pattern')
    return fig1
def Evening_Doji_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Evening_Doji_Star'],name='Evening Doji Star'))
    fig1.update_layout(title='Evening Doji Star',xaxis_title='Time',yaxis_title='Evening Doji Star')
    return fig1
def Evening_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Evening_Star'],name='Evening Star'))
    fig1.update_layout(title='Evening Star',xaxis_title='Time',yaxis_title='Evening Star')
    return fig1
def UpDown_gap_side_by_side_white_lines_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['UpDown_gap_side_by_side_white_lines'],name='Up/Down-gap side-by-side white lines'))
    fig1.update_layout(title='Up/Down-gap side-by-side white lines',xaxis_title='Time',yaxis_title='Up/Down-gap side-by-side white lines')
    return fig1
def Gravestone_Doji_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Gravestone_Doji'],name='Gravestone Doji'))
    fig1.update_layout(title='Gravestone Doji',xaxis_title='Time',yaxis_title='Gravestone Doji')
    return fig1
def Hammer_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Hammer'],name='Hammer'))
    fig1.update_layout(title='Hammer',xaxis_title='Time',yaxis_title='Hammer')
    return fig1
def Hanging_Man_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Hanging_Man'],name='Hanging Man'))
    fig1.update_layout(title='Hanging Man',xaxis_title='Time',yaxis_title='Hanging Man')
    return fig1
def Harami_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Harami_Pattern'],name='Harami Pattern'))
    fig1.update_layout(title='Harami Pattern',xaxis_title='Time',yaxis_title='Harami Pattern')
    return fig1
def Harami_Cross_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Harami_Cross_Pattern'],name='Harami Cross Pattern'))
    fig1.update_layout(title='Harami Cross Pattern',xaxis_title='Time',yaxis_title='Harami Cross Pattern')
    return fig1
def High_Wave_Candle_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['High_Wave_Candle'],name='High-Wave Candle'))
    fig1.update_layout(title='High-Wave Candle',xaxis_title='Time',yaxis_title='High-Wave Candle')
    return fig1
def Hikkake_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Hikkake_Pattern'],name='Hikkake Pattern'))
    fig1.update_layout(title='Hikkake Pattern',xaxis_title='Time',yaxis_title='Hikkake Pattern')
    return fig1
def Modified_Hikkake_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Modified_Hikkake_Pattern'],name='Modified Hikkake Pattern'))
    fig1.update_layout(title='Modified Hikkake Pattern',xaxis_title='Time',yaxis_title='Modified Hikkake Pattern')
    return fig1
def Homing_Pigeon_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Homing_Pigeon'],name='Homing Pigeon'))
    fig1.update_layout(title='Homing Pigeon',xaxis_title='Time',yaxis_title='Homing Pigeon')
    return fig1
def Identical_Three_Crows_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Identical_Three_Crows'],name='Identical Three Crows'))
    fig1.update_layout(title='Identical Three Crows',xaxis_title='Time',yaxis_title='Identical Three Crows')
    return fig1
def In_Neck_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['In_Neck_Pattern'],name='In-Neck Pattern'))
    fig1.update_layout(title='In-Neck Pattern',xaxis_title='Time',yaxis_title='In-Neck Pattern')
    return fig1
def Inverted_Hammer_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Inverted_Hammer'],name='Inverted Hammer'))
    fig1.update_layout(title='Inverted Hammer',xaxis_title='Time',yaxis_title='Inverted Hammer')
    return fig1
def Kicking_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Kicking'],name='Kicking'))
    fig1.update_layout(title='Kicking',xaxis_title='Time',yaxis_title='Kicking')
    return fig1
def Kicking___bullbear_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Kicking___bullbear'],name='Kicking - bull/bear'))
    fig1.update_layout(title='Kicking - bull/bear',xaxis_title='Time',yaxis_title='Kicking - bull/bear')
    return fig1
def Ladder_Bottom_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Ladder_Bottom'],name='Ladder Bottom'))
    fig1.update_layout(title='Ladder Bottom',xaxis_title='Time',yaxis_title='Ladder Bottom')
    return fig1
def Long_Legged_Doji_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Long_Legged_Doji'],name='Long Legged Doji'))
    fig1.update_layout(title='Long Legged Doji',xaxis_title='Time',yaxis_title='Long Legged Doji')
    return fig1
def Long_Line_Candle_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Long_Line_Candle'],name='Long Line Candle'))
    fig1.update_layout(title='Long Line Candle',xaxis_title='Time',yaxis_title='Long Line Candle')
    return fig1
def Marubozu_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Marubozu'],name='Marubozu'))
    fig1.update_layout(title='Marubozu',xaxis_title='Time',yaxis_title='Marubozu')
    return fig1
def Matching_Low_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Matching_Low'],name='Matching Low'))
    fig1.update_layout(title='Matching Low',xaxis_title='Time',yaxis_title='Matching Low')
    return fig1
def Mat_Hold_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Mat_Hold'],name='Mat Hold'))
    fig1.update_layout(title='Mat Hold',xaxis_title='Time',yaxis_title='Mat Hold')
    return fig1
def Morning_Doji_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Morning_Doji_Star'],name='Morning Doji Star'))
    fig1.update_layout(title='Morning Doji Star',xaxis_title='Time',yaxis_title='Morning Doji Star')
    return fig1
def Morning_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Morning_Star'],name='Morning Star'))
    fig1.update_layout(title='Morning Star',xaxis_title='Time',yaxis_title='Morning Star')
    return fig1
def On_Neck_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['On_Neck_Pattern'],name='On-Neck Pattern'))
    fig1.update_layout(title='On-Neck Pattern',xaxis_title='Time',yaxis_title='On-Neck Pattern')
    return fig1
def Piercing_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Piercing_Pattern'],name='Piercing Pattern'))
    fig1.update_layout(title='Piercing Pattern',xaxis_title='Time',yaxis_title='Piercing Pattern')
    return fig1
def Rickshaw_Man_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Rickshaw_Man'],name='Rickshaw Man'))
    fig1.update_layout(title='Rickshaw Man',xaxis_title='Time',yaxis_title='Rickshaw Man')
    return fig1
def RisingFalling_Three_Methods_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['RisingFalling_Three_Methods'],name='Rising/Falling Three Methods'))
    fig1.update_layout(title='Rising/Falling Three Methods',xaxis_title='Time',yaxis_title='Rising/Falling Three Methods')
    return fig1
def Separating_Lines_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Separating_Lines'],name='Separating Lines'))
    fig1.update_layout(title='Separating Lines',xaxis_title='Time',yaxis_title='Separating Lines')
    return fig1
def Shooting_Star_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Shooting_Star'],name='Shooting Star'))
    fig1.update_layout(title='Shooting Star',xaxis_title='Time',yaxis_title='Shooting Star')
    return fig1
def Short_Line_Candle_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Short_Line_Candle'],name='Short Line Candle'))
    fig1.update_layout(title='Short Line Candle',xaxis_title='Time',yaxis_title='Short Line Candle')
    return fig1
def Spinning_Top_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Spinning_Top'],name='Spinning Top'))
    fig1.update_layout(title='Spinning Top',xaxis_title='Time',yaxis_title='Spinning Top')
    return fig1
def Stalled_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stalled_Pattern'],name='Stalled Pattern'))
    fig1.update_layout(title='Stalled Pattern',xaxis_title='Time',yaxis_title='Stalled Pattern')
    return fig1
def Stick_Sandwich_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stick_Sandwich'],name='Stick Sandwich'))
    fig1.update_layout(title='Stick Sandwich',xaxis_title='Time',yaxis_title='Stick Sandwich')
    return fig1
def Takuri_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Takuri'],name='Takuri'))
    fig1.update_layout(title='Takuri',xaxis_title='Time',yaxis_title='Takuri')
    return fig1
def Tasuki_Gap_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Tasuki_Gap'],name='Tasuki Gap'))
    fig1.update_layout(title='Tasuki Gap',xaxis_title='Time',yaxis_title='Tasuki Gap')
    return fig1
def Thrusting_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Thrusting_Pattern'],name='Thrusting Pattern'))
    fig1.update_layout(title='Thrusting Pattern',xaxis_title='Time',yaxis_title='Thrusting Pattern')
    return fig1
def Tristar_Pattern_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Tristar_Pattern'],name='Tristar Pattern'))
    fig1.update_layout(title='Tristar Pattern',xaxis_title='Time',yaxis_title='Tristar Pattern')
    return fig1
def Unique_3_River_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Unique_3_River'],name='Unique 3 River'))
    fig1.update_layout(title='Unique 3 River',xaxis_title='Time',yaxis_title='Unique 3 River')
    return fig1
def Upside_Gap_Two_Crows_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Upside_Gap_Two_Crows'],name='Upside Gap Two Crows'))
    fig1.update_layout(title='Upside Gap Two Crows',xaxis_title='Time',yaxis_title='Upside Gap Two Crows')
    return fig1
def UpsideDownside_Gap_Three_Methods_Plot():
    from technicalta import indicator_data_level_1
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_1()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['UpsideDownside_Gap_Three_Methods'],name='Upside/Downside Gap Three Methods'))
    fig1.update_layout(title='Upside/Downside Gap Three Methods',xaxis_title='Time',yaxis_title='Upside/Downside Gap Three Methods')
    return fig1
def Aroon_Plot():
    from technicalta import indicator_data_level_2
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_2()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Aroon_0'],name='Aroon_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Aroon_1'],name='Aroon_1'))
    fig1.update_layout(title='Aroon',xaxis_title='Time',yaxis_title='Aroon')
    return fig1
def MESA_Adaptive_Moving_Average_Plot():
    from technicalta import indicator_data_level_2
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_2()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['MESA_Adaptive_Moving_Average_0'],name='MESA Adaptive Moving Average_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['MESA_Adaptive_Moving_Average_1'],name='MESA Adaptive Moving Average_1'))
    fig1.update_layout(title='MESA Adaptive Moving Average',xaxis_title='Time',yaxis_title='MESA Adaptive Moving Average')
    return fig1
def Stochastic_Plot():
    from technicalta import indicator_data_level_2
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_2()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stochastic_0'],name='Stochastic_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stochastic_1'],name='Stochastic_1'))
    fig1.update_layout(title='Stochastic',xaxis_title='Time',yaxis_title='Stochastic')
    return fig1
def Stochastic_Fast_Plot():
    from technicalta import indicator_data_level_2
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_2()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stochastic_Fast_0'],name='Stochastic Fast_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stochastic_Fast_1'],name='Stochastic Fast_1'))
    fig1.update_layout(title='Stochastic Fast',xaxis_title='Time',yaxis_title='Stochastic Fast')
    return fig1
def Stochastic_Relative_Strength_Index_Plot():
    from technicalta import indicator_data_level_2
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_2()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stochastic_Relative_Strength_Index_0'],name='Stochastic Relative Strength Index_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Stochastic_Relative_Strength_Index_1'],name='Stochastic Relative Strength Index_1'))
    fig1.update_layout(title='Stochastic Relative Strength Index',xaxis_title='Time',yaxis_title='Stochastic Relative Strength Index')
    return fig1
def Bollinger_Bands_Plot():
    from technicalta import indicator_data_level_3
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_3()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Bollinger_Bands_0'],name='Bollinger Bands_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Bollinger_Bands_1'],name='Bollinger Bands_1'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Bollinger_Bands_2'],name='Bollinger Bands_1'))
    fig1.update_layout(title='Bollinger Bands',xaxis_title='Time',yaxis_title='Bollinger Bands')
    return fig1
def Moving_Average_Convergence_Divergence_Fix_Plot():
    from technicalta import indicator_data_level_3
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_3()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_Average_Convergence_Divergence_Fix_0'],name='Moving Average Convergence-Divergence Fix_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_Average_Convergence_Divergence_Fix_1'],name='Moving Average Convergence-Divergence Fix_1'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_Average_Convergence_Divergence_Fix_2'],name='Moving Average Convergence-Divergence Fix_1'))
    fig1.update_layout(title='Moving Average Convergence-Divergence Fix',xaxis_title='Time',yaxis_title='Moving Average Convergence-Divergence Fix')
    return fig1
def Moving_Average_Convergence_Divergence_Plot():
    from technicalta import indicator_data_level_3
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    df=indicator_data_level_3()
    df=df.reset_index()
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_Average_Convergence_Divergence_0'],name='Moving Average Convergence-Divergence_0'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_Average_Convergence_Divergence_1'],name='Moving Average Convergence-Divergence_1'))
    fig1.add_trace(go.Scatter(x=df['date'], y=df['Moving_Average_Convergence_Divergence_2'],name='Moving Average Convergence-Divergence_1'))
    fig1.update_layout(title='Moving Average Convergence-Divergence',xaxis_title='Time',yaxis_title='Moving Average Convergence-Divergence')
    return fig1

def technical_plotter(technical):
    from technicalta import texterconversion
    import json
    technical=texterconversion(technical)
    if technical == 'Double_Exponential_Moving_Average':
        tech=Double_Exponential_Moving_Average_Plot()
    elif technical == 'Exponential_Moving_Average':
        tech=Exponential_Moving_Average_Plot()
    elif technical == 'Hilbert_Transform___Instantaneous_Trendline':
        tech=Hilbert_Transform___Instantaneous_Trendline_Plot()
    elif technical == 'Kaufman_Adaptive_Moving_Average':
        tech=Kaufman_Adaptive_Moving_Average_Plot()
    elif technical == 'Moving_average':
        tech=Moving_average_Plot()
    elif technical == 'Moving_average_with_variable_period':
        tech=Moving_average_with_variable_period_Plot()
    elif technical == 'MidPoint_over_period':
        tech=MidPoint_over_period_Plot()
    elif technical == 'Midpoint_Price_over_period':
        tech=Midpoint_Price_over_period_Plot()
    elif technical == 'Parabolic_SAR':
        tech=Parabolic_SAR_Plot()
    elif technical == 'Parabolic_SAR___Extended':
        tech=Parabolic_SAR___Extended_Plot()
    elif technical == 'Simple_Moving_Average':
        tech=Simple_Moving_Average_Plot()
    elif technical == 'Triple_Exponential_Moving_Average_T3':
        tech=Triple_Exponential_Moving_Average_T3_Plot()
    elif technical == 'Triple_Exponential_Moving_Average':
        tech=Triple_Exponential_Moving_Average_Plot()
    elif technical == 'Triangular_Moving_Average':
        tech=Triangular_Moving_Average_Plot()
    elif technical == 'Weighted_Moving_Average':
        tech=Weighted_Moving_Average_Plot()
    elif technical == 'Average_Directional_Movement_Index':
        tech=Average_Directional_Movement_Index_Plot()
    elif technical == 'Average_Directional_Movement_Index_Rating':
        tech=Average_Directional_Movement_Index_Rating_Plot()
    elif technical == 'Absolute_Price_Oscillator':
        tech=Absolute_Price_Oscillator_Plot()
    elif technical == 'Aroon_Oscillator':
        tech=Aroon_Oscillator_Plot()
    elif technical == 'Balance_Of_Power':
        tech=Balance_Of_Power_Plot()
    elif technical == 'Commodity_Channel_Index':
        tech=Commodity_Channel_Index_Plot()
    elif technical == 'Chande_Momentum_Oscillator':
        tech=Chande_Momentum_Oscillator_Plot()
    elif technical == 'Directional_Movement_Index':
        tech=Directional_Movement_Index_Plot()
    elif technical == 'MACD_with_controllable_MA_type':
        tech=MACD_with_controllable_MA_type_Plot()
    elif technical == 'Money_Flow_Index':
        tech=Money_Flow_Index_Plot()
    elif technical == 'Minus_Directional_Indicator':
        tech=Minus_Directional_Indicator_Plot()
    elif technical == 'Minus_Directional_Movement':
        tech=Minus_Directional_Movement_Plot()
    elif technical == 'Momentum':
        tech=Momentum_Plot()
    elif technical == 'Plus_Directional_Indicator':
        tech=Plus_Directional_Indicator_Plot()
    elif technical == 'Plus_Directional_Movement':
        tech=Plus_Directional_Movement_Plot()
    elif technical == 'Percentage_Price_Oscillator':
        tech=Percentage_Price_Oscillator_Plot()
    elif technical == 'Rate_of_change':
        tech=Rate_of_change_Plot()
    elif technical == 'Rate_of_change_Percentage':
        tech=Rate_of_change_Percentage_Plot()
    elif technical == 'Rate_of_change_ratio':
        tech=Rate_of_change_ratio_Plot()
    elif technical == 'Rate_of_change_ratio_100_scale':
        tech=Rate_of_change_ratio_100_scale_Plot()
    elif technical == 'Relative_Strength_Index':
        tech=Relative_Strength_Index_Plot()
    elif technical == 'one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA':
        tech=one_day_Rate_Of_Change_ROC_of_a_Triple_Smooth_EMA_Plot()
    elif technical == 'Ultimate_Oscillator':
        tech=Ultimate_Oscillator_Plot()
    elif technical == 'Williams':
        tech=Williams_Plot()
    elif technical == 'Chaikin_AD_Line':
        tech=Chaikin_AD_Line_Plot()
    elif technical == 'Chaikin_AD_Oscillator':
        tech=Chaikin_AD_Oscillator_Plot()
    elif technical == 'On_Balance_Volume':
        tech=On_Balance_Volume_Plot()
    elif technical == 'Two_Crows':
        tech=Two_Crows_Plot()
    elif technical == 'Three_Black_Crows':
        tech=Three_Black_Crows_Plot()
    elif technical == 'Three_Inside_UpDown':
        tech=Three_Inside_UpDown_Plot()
    elif technical == 'Three_Line_Strike':
        tech=Three_Line_Strike_Plot()
    elif technical == 'Three_Outside_UpDown':
        tech=Three_Outside_UpDown_Plot()
    elif technical == 'Three_Stars_In_The_South':
        tech=Three_Stars_In_The_South_Plot()
    elif technical == 'Three_Advancing_White_Soldiers':
        tech=Three_Advancing_White_Soldiers_Plot()
    elif technical == 'Abandoned_Baby':
        tech=Abandoned_Baby_Plot()
    elif technical == 'Advance_Block':
        tech=Advance_Block_Plot()
    elif technical == 'Belt_hold':
        tech=Belt_hold_Plot()
    elif technical == 'Breakaway':
        tech=Breakaway_Plot()
    elif technical == 'Closing_Marubozu':
        tech=Closing_Marubozu_Plot()
    elif technical == 'Concealing_Baby_Swallow':
        tech=Concealing_Baby_Swallow_Plot()
    elif technical == 'Counterattack':
        tech=Counterattack_Plot()
    elif technical == 'Dark_Cloud_Cover':
        tech=Dark_Cloud_Cover_Plot()
    elif technical == 'Doji':
        tech=Doji_Plot()
    elif technical == 'Doji_Star':
        tech=Doji_Star_Plot()
    elif technical == 'Dragonfly_Doji':
        tech=Dragonfly_Doji_Plot()
    elif technical == 'Engulfing_Pattern':
        tech=Engulfing_Pattern_Plot()
    elif technical == 'Evening_Doji_Star':
        tech=Evening_Doji_Star_Plot()
    elif technical == 'Evening_Star':
        tech=Evening_Star_Plot()
    elif technical == 'UpDown_gap_side_by_side_white_lines':
        tech=UpDown_gap_side_by_side_white_lines_Plot()
    elif technical == 'Gravestone_Doji':
        tech=Gravestone_Doji_Plot()
    elif technical == 'Hammer':
        tech=Hammer_Plot()
    elif technical == 'Hanging_Man':
        tech=Hanging_Man_Plot()
    elif technical == 'Harami_Pattern':
        tech=Harami_Pattern_Plot()
    elif technical == 'Harami_Cross_Pattern':
        tech=Harami_Cross_Pattern_Plot()
    elif technical == 'High_Wave_Candle':
        tech=High_Wave_Candle_Plot()
    elif technical == 'Hikkake_Pattern':
        tech=Hikkake_Pattern_Plot()
    elif technical == 'Modified_Hikkake_Pattern':
        tech=Modified_Hikkake_Pattern_Plot()
    elif technical == 'Homing_Pigeon':
        tech=Homing_Pigeon_Plot()
    elif technical == 'Identical_Three_Crows':
        tech=Identical_Three_Crows_Plot()
    elif technical == 'In_Neck_Pattern':
        tech=In_Neck_Pattern_Plot()
    elif technical == 'Inverted_Hammer':
        tech=Inverted_Hammer_Plot()
    elif technical == 'Kicking':
        tech=Kicking_Plot()
    elif technical == 'Kicking___bullbear':
        tech=Kicking___bullbear_Plot()
    elif technical == 'Ladder_Bottom':
        tech=Ladder_Bottom_Plot()
    elif technical == 'Long_Legged_Doji':
        tech=Long_Legged_Doji_Plot()
    elif technical == 'Long_Line_Candle':
        tech=Long_Line_Candle_Plot()
    elif technical == 'Marubozu':
        tech=Marubozu_Plot()
    elif technical == 'Matching_Low':
        tech=Matching_Low_Plot()
    elif technical == 'Mat_Hold':
        tech=Mat_Hold_Plot()
    elif technical == 'Morning_Doji_Star':
        tech=Morning_Doji_Star_Plot()
    elif technical == 'Morning_Star':
        tech=Morning_Star_Plot()
    elif technical == 'On_Neck_Pattern':
        tech=On_Neck_Pattern_Plot()
    elif technical == 'Piercing_Pattern':
        tech=Piercing_Pattern_Plot()
    elif technical == 'Rickshaw_Man':
        tech=Rickshaw_Man_Plot()
    elif technical == 'RisingFalling_Three_Methods':
        tech=RisingFalling_Three_Methods_Plot()
    elif technical == 'Separating_Lines':
        tech=Separating_Lines_Plot()
    elif technical == 'Shooting_Star':
        tech=Shooting_Star_Plot()
    elif technical == 'Short_Line_Candle':
        tech=Short_Line_Candle_Plot()
    elif technical == 'Spinning_Top':
        tech=Spinning_Top_Plot()
    elif technical == 'Stalled_Pattern':
        tech=Stalled_Pattern_Plot()
    elif technical == 'Stick_Sandwich':
        tech=Stick_Sandwich_Plot()
    elif technical == 'Takuri':
        tech=Takuri_Plot()
    elif technical == 'Tasuki_Gap':
        tech=Tasuki_Gap_Plot()
    elif technical == 'Thrusting_Pattern':
        tech=Thrusting_Pattern_Plot()
    elif technical == 'Tristar_Pattern':
        tech=Tristar_Pattern_Plot()
    elif technical == 'Unique_3_River':
        tech=Unique_3_River_Plot()
    elif technical == 'Upside_Gap_Two_Crows':
        tech=Upside_Gap_Two_Crows_Plot()
    elif technical == 'UpsideDownside_Gap_Three_Methods':
        tech=UpsideDownside_Gap_Three_Methods_Plot()
    elif technical == 'Aroon':
        tech=Aroon_Plot()
    elif technical == 'MESA_Adaptive_Moving_Average':
        tech=MESA_Adaptive_Moving_Average_Plot()
    elif technical == 'Stochastic':
        tech=Stochastic_Plot()
    elif technical == 'Stochastic_Fast':
        tech=Stochastic_Fast_Plot()
    elif technical == 'Stochastic_Relative_Strength_Index':
        tech=Stochastic_Relative_Strength_Index_Plot()
    elif technical == 'Bollinger_Bands':
        tech=Bollinger_Bands_Plot()
    elif technical == 'Moving_Average_Convergence_Divergence_Fix':
        tech=Moving_Average_Convergence_Divergence_Fix_Plot()
    elif technical == 'Moving_Average_Convergence_Divergence':
        tech=Moving_Average_Convergence_Divergence_Plot()
    if tech:
        tech = json.dumps(tech, cls=plotly.utils.PlotlyJSONEncoder)
        return tech
    else:
        print("Error in Technical Plotter")


'''

for k in listof1:
    i=texterconversion(k)
    print("def {}_Plot():".format(i))
    print("    from technicalta import indicator_data_level_1")
    print("    from plotly.subplots import make_subplots")
    print("    import plotly.graph_objects as go")
    print("    df=indicator_data_level_1()")
    print("    df=df['{}']".format(i))
    print("    df=df.reset_index()")
    print("    fig1=go.Figure()")
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}'],name='{}'))".format(i,k))
    print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
    print("    return fig1")


for k in listof2:
    i=texterconversion(k)
    print("def {}_Plot():".format(i))
    print("    from technicalta import indicator_data_level_2")
    print("    from plotly.subplots import make_subplots")
    print("    import plotly.graph_objects as go")
    print("    df=indicator_data_level_2()")
    print("    df=df['{}_0']".format(i))
    print("    df=df['{}_1']".format(i))
    print("    df=df.reset_index()")
    print("    fig1=go.Figure()")
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_0'],name='{}_0'))".format(i,k))
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_1'],name='{}_1'))".format(i,k))
    print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
    print("    return fig1")
for k in listof3:
    i=texterconversion(k)
    print("def {}_Plot():".format(i))
    print("    from technicalta import indicator_data_level_3")
    print("    from plotly.subplots import make_subplots")
    print("    import plotly.graph_objects as go")
    print("    df=indicator_data_level_3()")
    print("    df=df['{}_0']".format(i))
    print("    df=df['{}_1']".format(i))
    print("    df=df['{}_2']".format(i))
    print("    df=df.reset_index()")
    print("    fig1=go.Figure()")
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_0'],name='{}_0'))".format(i,k))
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_1'],name='{}_1'))".format(i,k))
    print("    fig1.add_trace(go.Scatter(x=df['date'], y=df['{}_2'],name='{}_1'))".format(i,k))
    print("    fig1.update_layout(title='{}',xaxis_title='Time',yaxis_title='{}')".format(k,k))
    print("    return fig1")
'''