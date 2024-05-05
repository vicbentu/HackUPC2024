import './App.css';
import VisitForm from './components/VisitForm/VisitForm';
import { Navbar } from './components/Navbar/Navbar';
import { Plan } from './components/Plan/Plan';
import { useState } from 'react';

function App() {
  const [plans_, setPlans_] = useState([]);

  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <VisitForm setPlans={setPlans_}/>
        <Plan plans={plans_} setPlans={setPlans_}/>
      </header>
    </div>
  );
}

export default App;
