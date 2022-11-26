import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LandingPage from './helpers/LandingPage';
import ClosetsList from './closets/ClosetsList';
import ClosetDetails from './closets/ClosetDetails';
import OutfitsList from './outfits/OutfitsList';
import OutfitDetails from './outfits/OutfitDetails';
import Nav from './helpers/Nav';

export default function App() {
  return (
    <BrowserRouter>
    <Nav />
      <div>
        <Routes>
          <Route path='/' element={<LandingPage />} />
          <Route path='closets/'>
            <Route path=''  element={<ClosetsList />} />
            <Route path='details/' element={<ClosetDetails />} />
          </Route>
          <Route path='outfits/'>
            <Route path='' element={<OutfitsList />} />
            <Route path='details/' element={<OutfitDetails />} />
          </Route>
          {/* <Route path='clothing/'>
            <Route path='' element={}>
            <Route>
          </Route> */}
      </Routes>
    </div>
    </BrowserRouter >
  );
};
