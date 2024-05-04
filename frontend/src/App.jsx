import './App.css';
import VisitForm from './components/VisitForm/VisitForm';
import { Navbar } from './components/Navbar/Navbar';
import { Plan } from './components/Plan/Plan';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <VisitForm />
        <Plan />
      </header>
    </div>
  );
}

export default App;