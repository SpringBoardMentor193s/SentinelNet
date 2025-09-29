import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import confusion_matrix, roc_curve, auc
import numpy as np
import pandas as pd

def plot_confusion_matrix(y_true, y_pred, labels=None, title='Confusion Matrix'):
    """Create an interactive confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    
    if labels is None:
        labels = np.unique(np.concatenate([y_true, y_pred]))
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale='Blues',
        text=cm,
        texttemplate='%{text}',
        textfont={"size": 16},
        hovertemplate='Predicted: %{x}<br>Actual: %{y}<br>Count: %{z}<extra></extra>'
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Predicted Label',
        yaxis_title='Actual Label',
        width=600,
        height=600
    )
    
    return fig


def plot_roc_curve(y_true, y_pred_proba, title='ROC Curve'):
    """Create ROC curve"""
    fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=fpr, y=tpr,
        mode='lines',
        name=f'ROC curve (AUC = {roc_auc:.4f})',
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
        width=700,
        height=600,
        showlegend=True
    )
    
    return fig


def plot_feature_importance(importance_dict, top_n=20, title='Top Feature Importances'):
    """Plot feature importance"""
    # Sort by importance
    sorted_features = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    features, importances = zip(*sorted_features)
    
    fig = go.Figure(go.Bar(
        x=importances,
        y=features,
        orientation='h',
        marker=dict(color=importances, colorscale='Viridis')
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Importance',
        yaxis_title='Features',
        height=max(400, top_n * 25),
        width=800
    )
    
    return fig


def plot_prediction_distribution(predictions, title='Prediction Distribution'):
    """Plot distribution of predictions"""
    pred_counts = pd.Series(predictions).value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=pred_counts.index,
        values=pred_counts.values,
        hole=0.3,
        marker=dict(colors=px.colors.qualitative.Set3)
    )])
    
    fig.update_layout(
        title=title,
        width=600,
        height=500
    )
    
    return fig


def plot_metrics_comparison(metrics_dict, title='Model Performance Comparison'):
    """Compare metrics across different models"""
    models = list(metrics_dict.keys())
    metrics = list(metrics_dict[models[0]].keys())
    
    fig = go.Figure()
    
    for metric in metrics:
        values = [metrics_dict[model][metric] for model in models]
        fig.add_trace(go.Bar(
            name=metric,
            x=models,
            y=values,
            text=[f'{v:.4f}' for v in values],
            textposition='auto'
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Model',
        yaxis_title='Score',
        barmode='group',
        width=900,
        height=500
    )
    
    return fig


def create_attack_type_chart(predictions, dataset_type='nsl_kdd'):
    """Create pie chart for attack type distribution"""
    attack_counts = pd.Series(predictions).value_counts()
    
    colors = {
        'Normal': '#2ecc71',
        'Benign': '#2ecc71',
        'DoS': '#e74c3c',
        'Probe': '#f39c12',
        'R2L': '#9b59b6',
        'U2R': '#e67e22',
        'Attack': '#c0392b'
    }
    
    fig = go.Figure(data=[go.Pie(
        labels=attack_counts.index,
        values=attack_counts.values,
        hole=0.4,
        marker=dict(colors=[colors.get(label, '#95a5a6') for label in attack_counts.index]),
        textinfo='label+percent',
        textfont_size=14
    )])
    
    fig.update_layout(
        title='Attack Type Distribution',
        width=700,
        height=500,
        showlegend=True
    )
    
    return fig


def plot_model_performance_radar(metrics_dict, title='Model Performance Radar Chart'):
    """Create radar chart for model performance comparison"""
    metrics = list(list(metrics_dict.values())[0].keys())
    
    fig = go.Figure()
    
    for model_name, model_metrics in metrics_dict.items():
        values = [model_metrics[m] for m in metrics]
        values.append(values[0])  # Close the radar chart
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=metrics + [metrics[0]],
            fill='toself',
            name=model_name
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        title=title,
        showlegend=True,
        width=700,
        height=600
    )
    
    return fig