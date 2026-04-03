import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { motion } from 'framer-motion'
import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

const API_BASE = import.meta.env.PROD ? '' : 'http://localhost:8000'

function App() {
  const [profile, setProfile] = useState(null)
  const [githubRepos, setGithubRepos] = useState([])
  const [loading, setLoading] = useState(true)
  const [darkMode, setDarkMode] = useState(false)
  const [formData, setFormData] = useState({ name: '', email: '', subject: '', message: '' })

  // Fetch data
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [profileRes, reposRes] = await Promise.all([
          axios.get(`${API_BASE}/api/profile`),
          axios.get(`${API_BASE}/api/github/repos`)
        ])
        setProfile(profileRes.data)
        setGithubRepos(reposRes.data)
      } catch (error) {
        console.error('Error fetching data:', error)
      } finally {
        setLoading(false)
      }
    }
    fetchData()

    // Dark mode from localStorage
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme === 'dark') {
      setDarkMode(true)
      document.documentElement.classList.add('dark')
    }
  }, [])

  // Toggle dark mode
  const toggleDarkMode = () => {
    setDarkMode(!darkMode)
    if (!darkMode) {
      document.documentElement.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      document.documentElement.classList.remove('dark')
      localStorage.setItem('theme', 'light')
    }
  }

  // Handle contact form submission
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await axios.post(`${API_BASE}/api/contact`, formData)
      toast.success('Message sent successfully! I\'ll get back to you soon.')
      setFormData({ name: '', email: '', subject: '', message: '' })
    } catch (error) {
      toast.error('Failed to send message. Please try again.')
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-950">
        <div className="spinner"></div>
      </div>
    )
  }

  return (
    <div className="bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-gray-100 transition-colors duration-300">
      <ToastContainer position="bottom-right" theme={darkMode ? 'dark' : 'light'} />
      
      {/* Navigation */}
      <nav className="sticky top-0 z-50 backdrop-blur-xl bg-white/80 dark:bg-gray-900/80 border-b border-gray-200 dark:border-gray-800">
        <div className="container mx-auto px-6 py-4 flex justify-between items-center">
          <a href="#" className="text-2xl font-bold">
            <span className="gradient-text">Getaye</span>
            <span className="text-gray-800 dark:text-white">.dev</span>
          </a>
          <div className="flex items-center gap-6">
            <a href="#experience" className="hidden md:block hover:text-blue-500 transition">Experience</a>
            <a href="#projects" className="hidden md:block hover:text-blue-500 transition">Projects</a>
            <a href="#contact" className="hidden md:block hover:text-blue-500 transition">Contact</a>
            <button onClick={toggleDarkMode} className="p-2 rounded-full bg-gray-200 dark:bg-gray-700">
              {darkMode ? <i className="fas fa-sun text-yellow-300"></i> : <i className="fas fa-moon"></i>}
            </button>
            <a href={profile.social.github} target="_blank" className="hover:text-blue-500"><i className="fab fa-github text-xl"></i></a>
            <a href={profile.social.linkedin} target="_blank" className="hover:text-blue-500"><i className="fab fa-linkedin text-xl"></i></a>
          </div>
        </div>
      </nav>

      <main className="container mx-auto px-6 py-12 max-w-6xl">
        {/* Hero Section */}
        <motion.section initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} className="min-h-[80vh] flex flex-col justify-center text-center">
          <h1 className="text-5xl md:text-6xl font-extrabold">Getaye <span className="gradient-text">Fiseha Tadesse</span></h1>
          <div className="text-xl text-gray-600 dark:text-gray-300 mt-4 space-y-2">
            <p className="font-semibold">{profile.titles.join(' | ')}</p>
          </div>
          <p className="text-lg max-w-2xl mx-auto mt-6 text-gray-600 dark:text-gray-400">{profile.bio}</p>
          <div className="flex flex-wrap justify-center gap-4 mt-8">
            <a href="#contact" className="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-xl transition">Send Message</a>
            <a href={profile.social.github} target="_blank" className="px-6 py-3 border border-gray-300 dark:border-gray-600 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-800 transition">GitHub Profile</a>
          </div>
        </motion.section>

        {/* Experience Section */}
        <section id="experience" className="py-16">
          <h2 className="text-3xl font-bold text-center mb-10">Work Experience</h2>
          <div className="grid md:grid-cols-2 gap-6">
            {profile.experiences.map((exp, idx) => (
              <motion.div key={idx} initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} transition={{ delay: idx * 0.1 }} className="bg-white dark:bg-gray-800/50 rounded-xl p-6 shadow-lg border-l-4 border-blue-500">
                <h3 className="text-xl font-bold">{exp.title}</h3>
                <p className="text-blue-600 dark:text-blue-400">{exp.company} | {exp.period}</p>
                <p className="text-sm text-gray-500 mt-1">{exp.location}</p>
                <p className="text-gray-600 dark:text-gray-300 text-sm mt-3">{exp.description}</p>
              </motion.div>
            ))}
          </div>
        </section>

        {/* Skills Section */}
        <section className="py-8">
          <h2 className="text-3xl font-bold text-center mb-8">Technical Skills</h2>
          <div className="flex flex-wrap justify-center gap-3">
            {profile.skills.map((skill, idx) => (
              <span key={idx} className="px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full text-sm font-medium hover:bg-blue-500 hover:text-white transition cursor-pointer">{skill}</span>
            ))}
          </div>
        </section>

        {/* Certifications */}
        <section className="py-12">
          <h2 className="text-3xl font-bold text-center mb-10">Certifications</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {profile.certifications.map((cert, idx) => (
              <div key={idx} className="bg-white dark:bg-gray-800/50 rounded-lg p-4 shadow-md">
                <i className="fas fa-certificate text-green-500 mr-2"></i>
                <span className="font-semibold">{cert.name}</span>
                <p className="text-sm text-gray-500 mt-1">{cert.issuer} • {cert.year}</p>
              </div>
            ))}
          </div>
        </section>

        {/* GitHub Projects */}
        <section id="projects" className="py-12">
          <h2 className="text-3xl font-bold text-center mb-10">GitHub Projects</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {githubRepos.map((repo, idx) => (
              <motion.div key={idx} whileHover={{ y: -5 }} className="bg-white dark:bg-gray-800/50 rounded-xl p-6 shadow-lg">
                <h3 className="text-xl font-bold truncate">{repo.name}</h3>
                <p className="text-sm text-gray-500 mt-1">{repo.language}</p>
                <p className="text-gray-600 dark:text-gray-300 text-sm mt-2">{repo.description}</p>
                <div className="flex justify-between mt-4">
                  <span><i className="fas fa-star text-yellow-500"></i> {repo.stars}</span>
                  <span><i className="fas fa-code-branch"></i> {repo.forks}</span>
                  <a href={repo.url} target="_blank" className="text-blue-500 hover:underline">View →</a>
                </div>
              </motion.div>
            ))}
          </div>
        </section>

        {/* Contact Form */}
        <section id="contact" className="py-16">
          <div className="bg-white dark:bg-gray-800/50 rounded-2xl p-8 shadow-xl">
            <h2 className="text-3xl font-bold text-center mb-6">Send Me a Message</h2>
            <div className="grid md:grid-cols-2 gap-8">
              <div className="space-y-4">
                <div><i className="fas fa-envelope text-blue-500 w-6"></i> {profile.email}</div>
                <div><i className="fas fa-phone text-blue-500 w-6"></i> {profile.phone}</div>
                <div><i className="fas fa-map-marker-alt text-blue-500 w-6"></i> {profile.location}</div>
              </div>
              <form onSubmit={handleSubmit} className="space-y-4">
                <input type="text" placeholder="Your Name" value={formData.name} onChange={(e) => setFormData({...formData, name: e.target.value})} required className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-900" />
                <input type="email" placeholder="Your Email" value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value})} required className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-900" />
                <input type="text" placeholder="Subject" value={formData.subject} onChange={(e) => setFormData({...formData, subject: e.target.value})} required className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-900" />
                <textarea rows="3" placeholder="Your Message" value={formData.message} onChange={(e) => setFormData({...formData, message: e.target.value})} required className="w-full px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-900"></textarea>
                <button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg transition">Send Message</button>
              </form>
            </div>
          </div>
        </section>

        <footer className="text-center py-8 text-gray-500 text-sm border-t border-gray-200 dark:border-gray-800">
          <p>© 2025 Getaye Fiseha Tadesse — System Administrator | Full Stack Developer | AI Engineer | Network Engineer</p>
        </footer>
      </main>
    </div>
  )
}

export default App
