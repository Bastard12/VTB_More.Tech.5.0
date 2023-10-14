import {
  createBrowserRouter, Link, NavLink, Outlet,
  RouterProvider,
} from "react-router-dom";
import {Navbar} from "./components/Navbar";



function App() {
  return (
      <div className="Outlet min-h-[100vh]">
        <div className="min-h-full">
          <Navbar/>
          <main>
            <div className="mx-auto">
              <Outlet />
            </div>
          </main>
        </div>
      </div>
  );
}

export default App;
