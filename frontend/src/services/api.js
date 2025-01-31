// {
//   "first_name": "Fred",
//   "last_name": "Pekyi",
//   "email": "fredpekyi01@gmail.com",
//   "role": {
//     "display": "admin"
//   }
// }
import axios from "axios";
import {toast} from "react-hot-toast";


const domain = 'https://eof8bhrbv0a1q08.m.pipedream.net/';

const handleSignup = async (formData) => {
    
try {
  // const response = await fetch(`${domain}user/register`, {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify({
  //     name: formData.name,
  //     nationality: formData.nationality, 
  //     email: formData.email,
  //     password: formData.password
  //   })
  // });

  const response = await axios.post(`${domain}user/register`, {
    name: formData.name,
    nationality: formData.nationality,
    email: formData.email,
    password: formData.password
  });

  console.log("response:", response);

  if (!response.status === 200) {
    throw new Error('Signup failed');
  }


  toast.success("Signup successful");
  const data = response.data;
  return data;

} catch (error) {
  console.error('Error during signup:', error);
  toast.error("Signup failed");
  throw error;
}
}

const handleLogin = async (formData) => {
    try {
        const response = await fetch(`${domain}user/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: formData.email,
                password: formData.password
            })
        });
        if (!response.ok) {
          throw new Error('Signup failed');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error during login:', error);
        throw error;
    }
}

const getEvents = async () => {
    try {
        const response = await axios.get(`${domain}events`);


        if (!response.ok) {
            throw new Error('Failed to fetch events');
        }

        const data = await response.data;
        toast.success("Events fetched successfully")
        return data;
    } catch (error) {
        console.error('Error fetching events:', error);
        throw error;
    }

}

const getEventById = async (id) => {
    try {
        const response = await axios.get(`${domain}events/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching event by id:', error);
        throw error;

    }
}


export { handleSignup, handleLogin, getEvents, getEventById };