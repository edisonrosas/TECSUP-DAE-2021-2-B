import React from 'react'


const Users = () =>{
    let params = useParams();
    return (
    <div>
        <h1>Usuarios</h1>
        <p>{params.id}</p>
    </div>)

}

export default Users;
//class Users extends React.Component {
//  render() {
//   return <h1>Usuarios</h1>
//  }
//}