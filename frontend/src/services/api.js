// {
//   "first_name": "Fred",
//   "last_name": "Pekyi",
//   "email": "fredpekyi01@gmail.com",
//   "role": {
//     "display": "admin"
//   }
// }



const domain = "https://speakwise.onrender.com/api/";

const handleSignup = async (formData) => {
    
try {
  const response = await fetch(`${domain}user/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: formData.name,
      nationality: formData.nationality, 
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
  console.error('Error during signup:', error);
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
        const response = await fetch(`${domain}/events`);

        if (!response.ok) {
            throw new Error('Failed to fetch events');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching events:', error);
        throw error;
    }
}


export { handleSignup, handleLogin, getEvents };