Python 3.12.10 (v3.12.10:0cc81280367, Apr  8 2025, 08:47:00) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Enter "help" below or click "Help" above for more information.
import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration
st.set_page_config(
    page_title="SubTrack - Subscription Tracker & Cancellation App",
    layout="wide"
)

# Embed your HTML content (including styles)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SubTrack - Subscription Tracker & Cancellation App</title>
    <style>
        :root {
            --primary: #7FC7AF;
            --primary-dark: #5BA88A;
            --secondary: #3F7366;
            --accent: #FF6B6B;
            --light: #f8f9fa;
            --dark: #212529;
            --text-dark: #333333;
            --text-light: #666666;
            --bg-light: #F5F7F9;
            --border-light: #E0E5E9;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: var(--bg-light);
            color: var(--text-dark);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: var(--primary);
            color: white;
            padding: 15px 0;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
            font-size: 28px;
            font-weight: bold;
        }
        
        .logo-icon {
            margin-right: 15px;
            font-size: 32px;
        }
        
        nav ul {
            display: flex;
            list-style: none;
        }
        
        nav ul li {
            margin-left: 25px;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        nav ul li a:hover {
            color: var(--secondary);
        }
        
        .user-profile {
            display: flex;
            align-items: center;
        }
        
        .user-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: #fff;
            margin-right: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
            font-weight: bold;
        }
        
        .dashboard {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 20px;
            margin-top: 20px;
        }
        
        .sidebar {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            height: fit-content;
        }
        
        .sidebar-section {
            margin-bottom: 25px;
        }
        
        .sidebar-title {
            font-size: 18px;
            margin-bottom: 15px;
            color: var(--text-dark);
            font-weight: 600;
        }
        
        .sidebar-menu {
            list-style: none;
        }
        
        .sidebar-menu li {
            margin-bottom: 12px;
        }
        
        .sidebar-menu a {
            display: flex;
            align-items: center;
            text-decoration: none;
            color: var(--text-light);
            font-weight: 500;
            padding: 8px 12px;
            border-radius: 6px;
            transition: all 0.3s;
        }
        
        .sidebar-menu a.active {
            background-color: rgba(127, 199, 175, 0.15);
            color: var(--primary-dark);
        }
        
        .sidebar-menu a:hover {
            background-color: rgba(127, 199, 175, 0.1);
            color: var(--primary-dark);
        }
        
        .menu-icon {
            margin-right: 10px;
            font-size: 18px;
        }
        
        .profile-section {
            padding: 15px;
            background-color: rgba(127, 199, 175, 0.1);
            border-radius: 8px;
        }
        
        .profile-info {
            font-size: 14px;
            margin-top: 5px;
            color: var(--text-light);
        }
        
        .main-content {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        .stats-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }
        
        .card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .stat-card {
            display: flex;
            flex-direction: column;
        }
        
        .stat-title {
            font-size: 14px;
            color: var(--text-light);
            margin-bottom: 10px;
        }
        
        .stat-value {
            font-size: 28px;
            font-weight: bold;
            color: var(--text-dark);
        }
        
        .stat-change {
            margin-top: 5px;
            font-size: 12px;
        }
        
        .positive-change {
            color: #2ecc71;
        }
        
        .negative-change {
            color: var(--accent);
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .card-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text-dark);
        }
        
        .table-container {
            overflow-x: auto;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-light);
        }
        
        th {
            font-weight: 600;
            color: var(--text-light);
            background-color: var(--bg-light);
        }
        
        tr:hover {
            background-color: rgba(127, 199, 175, 0.05);
        }
        
        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 50px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .badge-active {
            background-color: rgba(46, 204, 113, 0.15);
            color: #2ecc71;
        }
        
        .badge-inactive {
            background-color: rgba(231, 76, 60, 0.15);
            color: #e74c3c;
        }
        
        .badge-warning {
            background-color: rgba(255, 107, 107, 0.15);
            color: var(--accent);
        }
        
        .action-btn {
            background: none;
            border: none;
            color: var(--primary-dark);
            cursor: pointer;
            font-size: 14px;
            margin-right: 5px;
        }
        
        .chart-container {
            height: 300px;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #fff;
            border-radius: 8px;
        }
        
        .chart-placeholder {
            width: 100%;
            height: 250px;
            background-color: #f9f9f9;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #888;
            font-weight: 500;
        }
        
        .alert-card {
            display: flex;
            padding: 15px;
            background-color: rgba(255, 107, 107, 0.1);
            border-left: 4px solid var(--accent);
            margin-bottom: 15px;
            border-radius: 4px;
        }
        
        .alert-icon {
            margin-right: 15px;
            color: var(--accent);
            font-size: 20px;
        }
        
        .alert-content h4 {
            color: var(--text-dark);
            margin-bottom: 5px;
            font-size: 16px;
        }
        
        .alert-content p {
            color: var(--text-light);
            font-size: 14px;
            margin-bottom: 5px;
        }
        
        .alert-actions {
            margin-top: 5px;
        }
        
        .btn {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.3s;
            border: none;
        }
        
        .btn-primary {
            background-color: var(--primary);
            color: white;
        }
        
        .btn-primary:hover {
            background-color: var(--primary-dark);
        }
        
        .btn-accent {
            background-color: var(--accent);
            color: white;
        }
        
        .btn-accent:hover {
            background-color: #e55757;
        }
        
        .btn-outline {
            background-color: transparent;
            border: 1px solid #ddd;
            color: var(--text-light);
        }
        
        .btn-outline:hover {
            background-color: #f5f5f5;
        }
        
        .btn-sm {
            padding: 5px 10px;
            font-size: 12px;
        }
        
        .calendar-view {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 5px;
        }
        
        .calendar-day {
            padding: 10px;
            text-align: center;
            background-color: #f9f9f9;
            border-radius: 5px;
            font-size: 14px;
        }
        
        .has-event {
            background-color: rgba(127, 199, 175, 0.15);
            color: var(--primary-dark);
            font-weight: 500;
        }
        
        .app-logo {
            display: inline-block;
            margin-bottom: 10px;
        }
        
        .app-logo img {
            height: 36px;
        }
        
        .top-banner {
            background-color: var(--primary);
            color: white;
            text-align: center;
            padding: 8px;
            font-size: 14px;
            font-weight: 500;
        }
        
        .top-banner a {
            color: white;
            text-decoration: underline;
        }
        
        @media (max-width: 992px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="top-banner">
        Save up to 25% on your monthly subscriptions with SubTrack Premium - <a href="#">Upgrade now</a>
    </div>
    
    <header>
        <div class="container header-content">
            <div class="logo">
                <span class="logo-icon">📅</span>
                <span>SubTrack</span>
            </div>
            <nav>
                <ul>
                    <li><a href="#" class="active">Dashboard</a></li>
                    <li><a href="#">My Subscriptions</a></li>
                    <li><a href="#">Analytics</a></li>
                    <li><a href="#">Settings</a></li>
                </ul>
            </nav>
            <div class="user-profile">
                <div class="user-avatar">JS</div>
                <span>John Smith</span>
            </div>
        </div>
    </header>

    <div class="container">
        <div class="dashboard">
            <div class="sidebar">
                <div class="sidebar-section profile-section">
                    <div class="sidebar-title">Your Profile</div>
                    <div class="profile-info">
                        <p>Age: 21</p>
                        <p>Monthly Income: €1,200</p>
                        <p>Total Subscriptions: 6</p>
                    </div>
                </div>
                
                <div class="sidebar-section">
                    <div class="sidebar-title">Navigation</div>
                    <ul class="sidebar-menu">
                        <li><a href="#" class="active"><span class="menu-icon">📊</span> Dashboard</a></li>
                        <li><a href="#"><span class="menu-icon">📋</span> My Subscriptions</a></li>
                        <li><a href="#"><span class="menu-icon">📈</span> Spending Analysis</a></li>
                        <li><a href="#"><span class="menu-icon">⏰</span> Reminders</a></li>
                        <li><a href="#"><span class="menu-icon">🔍</span> Find Savings</a></li>
                        <li><a href="#"><span class="menu-icon">🎁</span> Free Trials</a></li>
                    </ul>
                </div>
                
                <div class="sidebar-section">
                    <div class="sidebar-title">Subscription Categories</div>
                    <ul class="sidebar-menu">
                        <li><a href="#"><span class="menu-icon">🎬</span> Entertainment</a></li>
                        <li><a href="#"><span class="menu-icon">🎵</span> Music</a></li>
                        <li><a href="#"><span class="menu-icon">🎮</span> Gaming</a></li>
                        <li><a href="#"><span class="menu-icon">💪</span> Fitness</a></li>
                        <li><a href="#"><span class="menu-icon">📚</span> Education</a></li>
                        <li><a href="#"><span class="menu-icon">➕</span> Others</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="main-content">
                <div class="alert-card">
                    <div class="alert-icon">⚠️</div>
                    <div class="alert-content">
                        <h4>Forgotten Subscription Detected!</h4>
                        <p>You haven't used your Spotify Premium subscription in 3 months but are still paying €9.99/month.</p>
                        <div class="alert-actions">
                            <button class="btn btn-accent btn-sm">Cancel Subscription</button>
                            <button class="btn btn-outline btn-sm">Remind Later</button>
                        </div>
                    </div>
                </div>
                
                <div class="stats-cards">
                    <div class="card stat-card">
                        <div class="stat-title">Monthly Subscription Cost</div>
                        <div class="stat-value">€48.99</div>
                        <div class="stat-change negative-change">+12% from last month</div>
                    </div>
                    
                    <div class="card stat-card">
                        <div class="stat-title">Average Usage</div>
                        <div class="stat-value">21.5 hrs</div>
                        <div class="stat-change positive-change">+3.2 hrs from last month</div>
                    </div>
                    
                    <div class="card stat-card">
                        <div class="stat-title">Active Subscriptions</div>
                        <div class="stat-value">6</div>
                        <div class="stat-change negative-change">+1 from last month</div>
                    </div>
                    
                    <div class="card stat-card">
                        <div class="stat-title">Savings Opportunity</div>
                        <div class="stat-value">€17.99</div>
                        <div class="stat-change">From 2 unused services</div>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">Your Subscriptions</div>
                        <button class="btn btn-primary btn-sm">+ Add New</button>
                    </div>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Service</th>
                                    <th>Category</th>
                                    <th>Monthly Cost</th>
                                    <th>Usage (hrs)</th>
                                    <th>Status</th>
                                    <th>Next Billing</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Netflix</td>
                                    <td>Entertainment</td>
                                    <td>€14.99</td>
                                    <td>12.5</td>
                                    <td><span class="badge badge-active">Active</span></td>
                                    <td>Apr 15, 2025</td>
                                    <td>
                                        <button class="action-btn">Edit</button>
                                        <button class="action-btn">Cancel</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Spotify Premium</td>
                                    <td>Music</td>
                                    <td>€9.99</td>
                                    <td>0.0</td>
                                    <td><span class="badge badge-warning">Forgotten</span></td>
                                    <td>Apr 22, 2025</td>
                                    <td>
                                        <button class="action-btn">Edit</button>
                                        <button class="action-btn">Cancel</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Disney+</td>
                                    <td>Entertainment</td>
                                    <td>€8.99</td>
                                    <td>4.2</td>
                                    <td><span class="badge badge-active">Active</span></td>
                                    <td>Apr 18, 2025</td>
                                    <td>
                                        <button class="action-btn">Edit</button>
                                        <button class="action-btn">Cancel</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Adobe Creative Cloud</td>
                                    <td>Education</td>
                                    <td>€19.99</td>
                                    <td>5.8</td>
                                    <td><span class="badge badge-active">Active</span></td>
                                    <td>Apr 30, 2025</td>
                                    <td>
                                        <button class="action-btn">Edit</button>
                                        <button class="action-btn">Cancel</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Xbox Game Pass</td>
                                    <td>Gaming</td>
                                    <td>€9.99</td>
                                    <td>0.0</td>
                                    <td><span class="badge badge-warning">Forgotten</span></td>
                                    <td>Apr 27, 2025</td>
                                    <td>
                                        <button class="action-btn">Edit</button>
                                        <button class="action-btn">Cancel</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>FitnessPal Pro</td>
                                    <td>Fitness</td>
                                    <td>€4.99</td>
                                    <td>3.2</td>
                                    <td><span class="badge badge-active">Active</span></td>
                                    <td>Apr 12, 2025</td>
                                    <td>
                                        <button class="action-btn">Edit</button>
                                        <button class="action-btn">Cancel</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">Subscription Spending Analysis</div>
                        <div>
                            <button class="btn btn-outline btn-sm">Monthly</button>
                            <button class="btn btn-outline btn-sm">Quarterly</button>
                            <button class="btn btn-outline btn-sm">Yearly</button>
                        </div>
                    </div>
                    <div class="chart-container">
                        <div class="chart-placeholder">
                            <img src="/api/placeholder/600/300" alt="Subscription Spending Trend Chart" />
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">Subscription Usage vs. Cost</div>
                    </div>
                    <div class="chart-container">
                        <div class="chart-placeholder">
                            <img src="/api/placeholder/600/300" alt="Usage vs Cost Analysis Chart" />
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">Upcoming Renewals</div>
                    </div>
                    <div class="calendar-view">
                        <div class="calendar-day">Mon</div>
                        <div class="calendar-day">Tue</div>
                        <div class="calendar-day">Wed</div>
                        <div class="calendar-day">Thu</div>
                        <div class="calendar-day">Fri</div>
                        <div class="calendar-day">Sat</div>
                        <div class="calendar-day">Sun</div>
                        
                        <div class="calendar-day">7</div>
                        <div class="calendar-day">8</div>
                        <div class="calendar-day">9</div>
                        <div class="calendar-day">10</div>
                        <div class="calendar-day">11</div>
                        <div class="calendar-day has-event">12 <br>FitnessPal</div>
                        <div class="calendar-day">13</div>
                        
                        <div class="calendar-day">14</div>
                        <div class="calendar-day has-event">15 <br>Netflix</div>
                        <div class="calendar-day">16</div>
                        <div class="calendar-day">17</div>
                        <div class="calendar-day has-event">18 <br>Disney+</div>
                        <div class="calendar-day">19</div>
                        <div class="calendar-day">20</div>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">Free Trial Tracker</div>
                    </div>
...                     <div class="table-container">
...                         <table>
...                             <thead>
...                                 <tr>
...                                     <th>Service</th>
...                                     <th>Start Date</th>
...                                     <th>End Date</th>
...                                     <th>Days Left</th>
...                                     <th>Will Convert To</th>
...                                     <th>Actions</th>
...                                 </tr>
...                             </thead>
...                             <tbody>
...                                 <tr>
...                                     <td>Audible Premium</td>
...                                     <td>Apr 1, 2025</td>
...                                     <td>Apr 30, 2025</td>
...                                     <td>22</td>
...                                     <td>€14.99/month</td>
...                                     <td>
...                                         <button class="btn btn-primary btn-sm">Set Reminder</button>
...                                         <button class="btn btn-accent btn-sm">Cancel Now</button>
...                                     </td>
...                                 </tr>
...                             </tbody>
...                         </table>
...                     </div>
...                 </div>
...             </div>
...         </div>
...     </div>
... </body>
... </html>
... """
... 
... # Render the HTML within the Streamlit app
... components.html(html_content, height=1500, scrolling=True)
