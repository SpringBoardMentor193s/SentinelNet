import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import confusion_matrix, roc_curve, auc
import numpy as np
import pandas as pd

def plot_confusion_matrix(y_true, y_pred, title="Confusion Matrix"):
    """Plot confusion matrix using Plotly"""
    cm = confusion_matrix(y_true, y_pred)
    
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=[f'Predicted {i}' for i in range(len(cm))],
        y=[f'Actual {i}' for i in range(len(cm))],
        colorscale='Blues',
        text=cm,
        texttemplate='%{text}',
        textfont={"size": 16},
        hovertemplate='Predicted: %{x}<br>Actual: %{y}<br>Count: %{z}<extra></extra>'
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Predicted Label",
        yaxis_title="True Label",
        height=500
    )
    
    return fig

def plot_roc_curve(y_true, y_score, title="ROC Curve"):
    """Plot ROC curve using Plotly"""
    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=fpr, y=tpr,
        mode='lines',
        name=f'ROC curve (AUC = {roc_auc:.2f})',
        line=dict(color='darkorange', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0, 1],
        mode='lines',
        name='Random Classifier',
        line=dict(color='navy', width=2, dash='dash')
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title='False Positive Rate',
        yaxis_title='True Positive Rate',
        height=500,
        showlegend=True
    )
    
    return fig

def plot_feature_importance(importance_dict, top_n=20, title="Feature Importance"):
    """Plot feature importance using Plotly"""
    sorted_features = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    features, importances = zip(*sorted_features)
    
    fig = go.Figure(data=[
        go.Bar(x=list(importances), y=list(features), orientation='h')
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="Importance",
        yaxis_title="Features",
        height=600,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig

def plot_prediction_distribution(predictions, title="Prediction Distribution"):
    """Plot distribution of predictions using Plotly"""
    pred_counts = pd.Series(predictions).value_counts()
    
    fig = go.Figure(data=[
        go.Pie(
            labels=pred_counts.index,
            values=pred_counts.values,
            hole=0.3,
            textinfo='label+percent',
            textfont_size=14
        )
    ])
    
    fig.update_layout(
        title=title,
        height=400
    )
    
    return fig

def plot_metrics_comparison(metrics_dict, title="Model Metrics Comparison"):
    """Plot comparison of different metrics"""
    fig = go.Figure()
    
    for metric_name, values in metrics_dict.items():
        fig.add_trace(go.Bar(
            name=metric_name,
            x=list(values.keys()),
            y=list(values.values())
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Models",
        yaxis_title="Score",
        barmode='group',
        height=500
    )
    
    return fig

def create_attack_type_chart(predictions, dataset_type='nsl_kdd', title="Attack Type Distribution"):
    """Create a bar chart for attack type distribution"""
    pred_counts = pd.Series(predictions).value_counts()
    
    colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']
    
    fig = go.Figure(data=[
        go.Bar(
            x=pred_counts.index,
            y=pred_counts.values,
            marker_color=colors[:len(pred_counts)],
            text=pred_counts.values,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="Attack Type",
        yaxis_title="Count",
        height=400,
        showlegend=False
    )
    
    return fig