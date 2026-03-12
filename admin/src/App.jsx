import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Users from './pages/Users';
import Jobs from './pages/Jobs';
import Transactions from './pages/Transactions';
import Disputes from './pages/Disputes';

function App() {
  return (
    <BrowserRouter>
      <div className="flex h-screen bg-gray-100">
        <Sidebar />
        <main className="flex-1 overflow-auto">
          <Routes>
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/users" element={<Users />} />
            <Route path="/jobs" element={<Jobs />} />
            <Route path="/transactions" element={<Transactions />} />
            <Route path="/disputes" element={<Disputes />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
