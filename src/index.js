const app = express()
const login = require('./screens/Login/login')

app.listen(PORT, async function () {
  console.log(`App listening on ${PORT} !`)
})

app.use('/login', login)

app.get('/', function (req, res) {
  return res.redirect('/login')
})